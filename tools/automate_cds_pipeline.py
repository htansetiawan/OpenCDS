#!/usr/bin/env python3
"""
Common Data Set Automation Pipeline
Processes PDF and Excel files, then commits and pushes to git repository.

Usage:
    python automate_cds_pipeline.py <input_folder> [options]
"""

import os
import sys
import subprocess
from pathlib import Path
import argparse
from datetime import datetime


class CDSAutomationPipeline:
    """Automate the entire CDS processing and git workflow."""

    def __init__(self, input_folder: str, output_folder: str, git_url: str = None,
                 dpi: int = 300, skip_git: bool = False):
        """
        Initialize the pipeline.

        Args:
            input_folder: Folder containing PDF and Excel files
            output_folder: Folder to save markdown files
            git_url: Git repository URL (optional, uses current repo if None)
            dpi: DPI for PDF conversion
            skip_git: Skip git operations
        """
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.git_url = git_url
        self.dpi = dpi
        self.skip_git = skip_git

        # Validate input folder
        if not self.input_folder.exists():
            raise FileNotFoundError(f"Input folder not found: {input_folder}")

        # Create output folder
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def run(self):
        """Execute the complete pipeline."""
        print("\n" + "=" * 70)
        print("COMMON DATA SET AUTOMATION PIPELINE")
        print("=" * 70)
        print(f"Input folder:  {self.input_folder.absolute()}")
        print(f"Output folder: {self.output_folder.absolute()}")
        if self.git_url:
            print(f"Git URL:       {self.git_url}")
        print("=" * 70 + "\n")

        # Step 1: Process Excel files
        print("STEP 1: Processing Excel files...")
        print("-" * 70)
        excel_success = self._process_excel_files()

        # Step 2: Process PDF files
        print("\nSTEP 2: Processing PDF files...")
        print("-" * 70)
        pdf_success = self._process_pdf_files()

        # Step 3: Git operations
        if not self.skip_git:
            print("\nSTEP 3: Git operations...")
            print("-" * 70)
            git_success = self._git_operations()
        else:
            print("\nSTEP 3: Git operations skipped (--skip-git flag)")
            git_success = True

        # Summary
        print("\n" + "=" * 70)
        print("PIPELINE SUMMARY")
        print("=" * 70)
        print(f"Excel processing:  {'✓ Success' if excel_success else '✗ Failed'}")
        print(f"PDF processing:    {'✓ Success' if pdf_success else '✗ Failed'}")
        print(f"Git operations:    {'✓ Success' if git_success else '✗ Failed/Skipped'}")
        print("=" * 70 + "\n")

        if excel_success and pdf_success and git_success:
            print("🎉 Pipeline completed successfully!")
            return 0
        else:
            print("⚠️  Pipeline completed with errors")
            return 1

    def _process_excel_files(self) -> bool:
        """Process all Excel files."""
        try:
            from xls_to_markdown import ExcelToMarkdownConverter

            converter = ExcelToMarkdownConverter(output_dir=str(self.output_folder))
            excel_files = []

            for pattern in ['*.xls', '*.xlsx', '*.xlsm']:
                excel_files.extend(sorted(self.input_folder.glob(pattern)))

            if not excel_files:
                print("  No Excel files found - skipping")
                return True

            print(f"  Found {len(excel_files)} Excel file(s)")

            for excel_file in excel_files:
                print(f"\n  Processing: {excel_file.name}")
                converter.process_file(str(excel_file))

            print(f"\n  ✓ Processed {len(excel_files)} Excel file(s)")
            return True

        except ImportError as e:
            print(f"  ✗ Error: Excel processing dependencies not installed")
            print(f"    Run: pip install openpyxl xlrd")
            return False
        except Exception as e:
            print(f"  ✗ Error processing Excel files: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _process_pdf_files(self) -> bool:
        """Process all PDF files."""
        try:
            from pdf_to_markdown import PDFToMarkdownConverter

            converter = PDFToMarkdownConverter(output_dir=str(self.output_folder))
            pdf_files = sorted(self.input_folder.glob("*.pdf"))

            if not pdf_files:
                print("  No PDF files found - skipping")
                return True

            print(f"  Found {len(pdf_files)} PDF file(s)")
            print(f"  Using DPI: {self.dpi}")

            for pdf_file in pdf_files:
                print(f"\n  Processing: {pdf_file.name}")
                converter.process_single_file(str(pdf_file))

            print(f"\n  ✓ Processed {len(pdf_files)} PDF file(s)")
            return True

        except ImportError as e:
            print(f"  ✗ Error: PDF processing dependencies not installed")
            print(f"    Run: pip install pytesseract Pillow pdf2image")
            print(f"    System deps: brew install tesseract poppler (macOS)")
            return False
        except Exception as e:
            print(f"  ✗ Error processing PDF files: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _git_operations(self) -> bool:
        """Handle git clone/pull, add, commit, and push."""
        try:
            # If git URL is provided, clone or update repository
            if self.git_url:
                success = self._setup_git_repo()
                if not success:
                    return False

            # Check if we're in a git repository
            result = subprocess.run(
                ['git', 'rev-parse', '--git-dir'],
                capture_output=True,
                text=True,
                cwd=self.output_folder.parent
            )

            if result.returncode != 0:
                print("  ✗ Not a git repository and no git URL provided")
                print("    Either provide --git-url or run in a git repository")
                return False

            # Stage the output files
            print("  Staging files...")
            subprocess.run(
                ['git', 'add', str(self.output_folder)],
                check=True,
                cwd=self.output_folder.parent
            )

            # Check if there are changes to commit
            result = subprocess.run(
                ['git', 'diff', '--cached', '--quiet'],
                cwd=self.output_folder.parent
            )

            if result.returncode == 0:
                print("  No changes to commit")
                return True

            # Create commit message
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_message = f"""Add Common Data Set markdown files

Processed on: {timestamp}
Source folder: {self.input_folder.name}

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"""

            # Commit changes
            print("  Creating commit...")
            subprocess.run(
                ['git', 'commit', '-m', commit_message],
                check=True,
                cwd=self.output_folder.parent
            )

            # Push to remote
            print("  Pushing to remote...")
            subprocess.run(
                ['git', 'push'],
                check=True,
                cwd=self.output_folder.parent
            )

            print("  ✓ Changes committed and pushed successfully")
            return True

        except subprocess.CalledProcessError as e:
            print(f"  ✗ Git operation failed: {e}")
            return False
        except Exception as e:
            print(f"  ✗ Error during git operations: {e}")
            import traceback
            traceback.print_exc()
            return False

    def _setup_git_repo(self) -> bool:
        """Clone or pull git repository."""
        try:
            repo_name = self.git_url.split('/')[-1].replace('.git', '')
            repo_path = self.output_folder.parent / repo_name

            if repo_path.exists():
                print(f"  Repository exists, pulling latest changes...")
                subprocess.run(
                    ['git', 'pull'],
                    check=True,
                    cwd=repo_path
                )
            else:
                print(f"  Cloning repository from {self.git_url}...")
                subprocess.run(
                    ['git', 'clone', self.git_url, str(repo_path)],
                    check=True
                )

            # Update output folder to be inside the repo
            self.output_folder = repo_path / self.output_folder.name
            self.output_folder.mkdir(parents=True, exist_ok=True)

            print(f"  ✓ Repository ready at: {repo_path}")
            return True

        except subprocess.CalledProcessError as e:
            print(f"  ✗ Failed to setup git repository: {e}")
            return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Automate Common Data Set processing and git workflow",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process files and commit to current repo
  python automate_cds_pipeline.py ./raw_files -o output

  # Process files and push to specific git repository
  python automate_cds_pipeline.py ./raw_files -o output --git-url https://github.com/user/repo.git

  # High-quality PDF processing
  python automate_cds_pipeline.py ./raw_files -o output --dpi 600

  # Process without git operations
  python automate_cds_pipeline.py ./raw_files -o output --skip-git
        """
    )

    parser.add_argument(
        'input_folder',
        help='Folder containing PDF and Excel files to process'
    )
    parser.add_argument(
        '-o', '--output-folder',
        default='output',
        help='Output folder for markdown files (default: output)'
    )
    parser.add_argument(
        '--git-url',
        help='Git repository URL to clone/push to (optional)'
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='DPI for PDF conversion (default: 300, try 600 for better quality)'
    )
    parser.add_argument(
        '--skip-git',
        action='store_true',
        help='Skip git operations (only process files)'
    )

    args = parser.parse_args()

    try:
        pipeline = CDSAutomationPipeline(
            input_folder=args.input_folder,
            output_folder=args.output_folder,
            git_url=args.git_url,
            dpi=args.dpi,
            skip_git=args.skip_git
        )
        exit_code = pipeline.run()
        sys.exit(exit_code)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nPipeline interrupted by user")
        sys.exit(130)
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
