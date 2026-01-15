#!/usr/bin/env python3
"""
Unified processor for all Common Data Set files.
Automatically detects file types and processes PDFs and Excel files.
"""

import os
import sys
from pathlib import Path
import argparse


def main():
    """Process all CDS files in a directory."""
    parser = argparse.ArgumentParser(
        description="Process all Common Data Set files (PDF, Excel) in a directory"
    )
    parser.add_argument(
        'input_dir',
        nargs='?',
        default='.',
        help='Directory containing CDS files (default: current directory)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        default='output',
        help='Output directory for markdown files (default: output)'
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='DPI for PDF conversion (default: 300, try 600 for better quality)'
    )
    parser.add_argument(
        '--pdf-only',
        action='store_true',
        help='Only process PDF files'
    )
    parser.add_argument(
        '--excel-only',
        action='store_true',
        help='Only process Excel files'
    )

    args = parser.parse_args()

    input_path = Path(args.input_dir)
    if not input_path.exists():
        print(f"Error: Directory not found: {args.input_dir}")
        sys.exit(1)

    # Find all relevant files
    pdf_files = []
    excel_files = []

    if not args.excel_only:
        pdf_files = sorted(input_path.glob("*.pdf"))

    if not args.pdf_only:
        for pattern in ['*.xls', '*.xlsx', '*.xlsm']:
            excel_files.extend(sorted(input_path.glob(pattern)))

    total_files = len(pdf_files) + len(excel_files)

    if total_files == 0:
        print(f"No PDF or Excel files found in {args.input_dir}")
        sys.exit(0)

    print(f"\nCommon Data Set Batch Processor")
    print(f"{'=' * 50}")
    print(f"Input directory: {input_path.absolute()}")
    print(f"Output directory: {args.output_dir}")
    print(f"Found {len(pdf_files)} PDF file(s)")
    print(f"Found {len(excel_files)} Excel file(s)")
    print(f"{'=' * 50}\n")

    # Process Excel files
    if excel_files:
        print("Processing Excel files...")
        print("-" * 50)
        try:
            from xls_to_markdown import ExcelToMarkdownConverter
            converter = ExcelToMarkdownConverter(output_dir=args.output_dir)

            for excel_file in excel_files:
                print(f"\n📊 {excel_file.name}")
                converter.process_file(str(excel_file))

        except ImportError as e:
            print(f"Error: Cannot import Excel converter: {e}")
            print("Make sure openpyxl and xlrd are installed:")
            print("  pip install openpyxl xlrd")
        except Exception as e:
            print(f"Error processing Excel files: {e}")

    # Process PDF files
    if pdf_files:
        print("\nProcessing PDF files...")
        print("-" * 50)
        try:
            from pdf_to_markdown import PDFToMarkdownConverter
            converter = PDFToMarkdownConverter(output_dir=args.output_dir)

            for pdf_file in pdf_files:
                print(f"\n📄 {pdf_file.name}")
                converter.process_single_file(str(pdf_file))

        except ImportError as e:
            print(f"Error: Cannot import PDF converter: {e}")
            print("Make sure required packages are installed:")
            print("  pip install pytesseract Pillow pdf2image")
            print("\nAlso install system dependencies:")
            print("  macOS: brew install tesseract poppler")
            print("  Ubuntu: sudo apt-get install tesseract-ocr poppler-utils")
        except Exception as e:
            print(f"Error processing PDF files: {e}")

    print(f"\n{'=' * 50}")
    print(f"✓ Processing complete!")
    print(f"Output files saved to: {Path(args.output_dir).absolute()}")
    print(f"{'=' * 50}\n")


if __name__ == "__main__":
    main()
