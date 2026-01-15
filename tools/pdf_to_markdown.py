#!/usr/bin/env python3
"""
PDF to Markdown Converter using Tesseract OCR with Table Detection
Processes PDFs one by one, extracts text via OCR, detects and formats tables.
"""

import os
import sys
from pathlib import Path
from typing import List, Optional, Dict, Tuple
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import re

# Optional table extraction libraries
try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False

try:
    import camelot
    CAMELOT_AVAILABLE = True
except ImportError:
    CAMELOT_AVAILABLE = False


class PDFToMarkdownConverter:
    """Convert PDF files to Markdown using Tesseract OCR."""

    def __init__(self, output_dir: str = "documents", extract_tables: bool = True):
        """
        Initialize the converter.

        Args:
            output_dir: Directory to save markdown files
            extract_tables: Whether to use specialized table extraction
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.extract_tables = extract_tables

        # Check available table extraction methods
        if extract_tables and not (PDFPLUMBER_AVAILABLE or CAMELOT_AVAILABLE):
            print("Warning: Table extraction libraries not available.")
            print("Install with: pip install pdfplumber camelot-py[cv]")
            print("Falling back to basic OCR.\n")

    def process_pdf(self, pdf_path: str, dpi: int = 300) -> str:
        """
        Process a single PDF file and convert to markdown.

        Args:
            pdf_path: Path to the PDF file
            dpi: DPI for PDF to image conversion (higher = better quality but slower)

        Returns:
            Extracted markdown text
        """
        print(f"Processing: {pdf_path}")

        # Try table extraction first if available
        tables_by_page = {}
        if self.extract_tables and (PDFPLUMBER_AVAILABLE or CAMELOT_AVAILABLE):
            print(f"  Extracting tables...")
            tables_by_page = self._extract_tables(pdf_path)
            if tables_by_page:
                print(f"  Found {sum(len(t) for t in tables_by_page.values())} table(s)")

        # Convert PDF to images
        print(f"  Converting PDF to images (DPI: {dpi})...")
        images = convert_from_path(pdf_path, dpi=dpi)
        print(f"  Found {len(images)} page(s)")

        # Extract text from each page
        markdown_content = []
        for i, image in enumerate(images, start=1):
            print(f"  OCR processing page {i}/{len(images)}...")
            text = pytesseract.image_to_string(image)

            # Add page separator if multiple pages
            if len(images) > 1:
                markdown_content.append(f"## Page {i}\n")

            # If we have tables for this page, try to integrate them
            if i in tables_by_page:
                formatted_text = self._format_with_tables(text, tables_by_page[i])
            else:
                # Clean and format the text normally
                formatted_text = self._format_as_markdown(text)

            markdown_content.append(formatted_text)
            markdown_content.append("\n")

        return "\n".join(markdown_content)

    def _format_as_markdown(self, text: str) -> str:
        """
        Format extracted text as proper markdown.

        Args:
            text: Raw OCR text

        Returns:
            Formatted markdown text
        """
        # Remove excessive whitespace
        lines = text.split('\n')
        formatted_lines = []

        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append("")
                continue

            # Detect potential headers (all caps or title case with few words)
            if self._is_likely_header(line):
                # Convert to header based on length/importance
                if len(line.split()) <= 5 and line.isupper():
                    formatted_lines.append(f"### {line.title()}")
                else:
                    formatted_lines.append(f"#### {line}")
            else:
                formatted_lines.append(line)

        # Remove multiple consecutive empty lines
        result = '\n'.join(formatted_lines)
        result = re.sub(r'\n{3,}', '\n\n', result)

        return result

    def _is_likely_header(self, line: str) -> bool:
        """
        Determine if a line is likely a header.

        Args:
            line: Text line to check

        Returns:
            True if likely a header
        """
        # Short lines in all caps
        if line.isupper() and len(line.split()) <= 6:
            return True

        # Lines that end with colon
        if line.endswith(':') and len(line.split()) <= 8:
            return True

        return False

    def _extract_tables(self, pdf_path: str) -> Dict[int, List[List[List[str]]]]:
        """
        Extract tables from PDF using specialized libraries.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Dictionary mapping page numbers to lists of tables
        """
        tables_by_page = {}

        # Try pdfplumber first (better for text-based PDFs)
        if PDFPLUMBER_AVAILABLE:
            try:
                with pdfplumber.open(pdf_path) as pdf:
                    for page_num, page in enumerate(pdf.pages, start=1):
                        tables = page.extract_tables()
                        if tables:
                            # Filter out empty tables
                            valid_tables = [t for t in tables if t and len(t) > 1]
                            if valid_tables:
                                tables_by_page[page_num] = valid_tables
            except Exception as e:
                print(f"  Warning: pdfplumber extraction failed: {e}")

        # If pdfplumber didn't work well, try camelot (better for scanned PDFs)
        if not tables_by_page and CAMELOT_AVAILABLE:
            try:
                # Try lattice mode first (for tables with borders)
                tables = camelot.read_pdf(pdf_path, pages='all', flavor='lattice')
                if len(tables) == 0:
                    # Fall back to stream mode (for tables without borders)
                    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')

                for table in tables:
                    page_num = table.page
                    if page_num not in tables_by_page:
                        tables_by_page[page_num] = []
                    # Convert to list format
                    tables_by_page[page_num].append(table.df.values.tolist())
            except Exception as e:
                print(f"  Warning: camelot extraction failed: {e}")

        return tables_by_page

    def _format_with_tables(self, text: str, tables: List[List[List[str]]]) -> str:
        """
        Format text with embedded tables.

        Args:
            text: OCR extracted text
            tables: List of tables for this page

        Returns:
            Formatted markdown with tables
        """
        # Format the basic text
        formatted_text = self._format_as_markdown(text)

        # Append tables at the end
        table_markdown = []
        for i, table in enumerate(tables, start=1):
            if len(tables) > 1:
                table_markdown.append(f"\n### Table {i}\n")
            table_markdown.append(self._table_to_markdown(table))

        return formatted_text + "\n" + "\n".join(table_markdown)

    def _table_to_markdown(self, table: List[List[str]]) -> str:
        """
        Convert table data to markdown format.

        Args:
            table: 2D list representing table data

        Returns:
            Markdown formatted table
        """
        if not table or len(table) < 1:
            return ""

        # Clean table data
        cleaned_table = []
        for row in table:
            cleaned_row = [str(cell).strip() if cell else "" for cell in row]
            cleaned_table.append(cleaned_row)

        # Calculate column widths
        num_cols = max(len(row) for row in cleaned_table)
        col_widths = [0] * num_cols

        for row in cleaned_table:
            for i, cell in enumerate(row):
                if i < num_cols:
                    col_widths[i] = max(col_widths[i], len(cell))

        # Build markdown table
        markdown_lines = []

        # Header row (use first row as header)
        if cleaned_table:
            header = cleaned_table[0]
            # Pad header to num_cols
            while len(header) < num_cols:
                header.append("")
            header_line = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(header[:num_cols])) + " |"
            markdown_lines.append(header_line)

            # Separator
            separator = "| " + " | ".join("-" * col_widths[i] for i in range(num_cols)) + " |"
            markdown_lines.append(separator)

            # Data rows
            for row in cleaned_table[1:]:
                # Pad row to num_cols
                while len(row) < num_cols:
                    row.append("")
                row_line = "| " + " | ".join(cell.ljust(col_widths[i]) for i, cell in enumerate(row[:num_cols])) + " |"
                markdown_lines.append(row_line)

        return "\n".join(markdown_lines)

    def process_directory(self, directory: str = ".", pattern: str = "*.pdf") -> None:
        """
        Process all PDF files in a directory.

        Args:
            directory: Directory containing PDF files
            pattern: Glob pattern for PDF files
        """
        pdf_dir = Path(directory)
        pdf_files = sorted(pdf_dir.glob(pattern))

        if not pdf_files:
            print(f"No PDF files found in {directory}")
            return

        print(f"Found {len(pdf_files)} PDF file(s)\n")

        # Track processing statistics
        processed_count = 0
        skipped_count = 0
        failed_count = 0

        for pdf_path in pdf_files:
            # Create tracking file paths
            processed_marker = self.output_dir / f".{pdf_path.stem}.processed"
            failed_marker = self.output_dir / f".{pdf_path.stem}.failed"
            output_file = self.output_dir / f"{pdf_path.stem}.md"

            # Skip if already processed successfully
            if processed_marker.exists() and output_file.exists():
                print(f"⊙ Skipping {pdf_path.name} (already processed)")
                skipped_count += 1
                continue

            # Remove old failed marker if retrying
            if failed_marker.exists():
                failed_marker.unlink()

            try:
                # Process the PDF
                markdown_text = self.process_pdf(str(pdf_path))

                # Save to markdown file
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(f"# {pdf_path.stem}\n\n")
                    f.write(markdown_text)

                # Create success marker
                with open(processed_marker, 'w') as f:
                    f.write(f"Processed on: {Path(pdf_path).stat().st_mtime}\n")
                    f.write(f"Output: {output_file}\n")

                print(f"  ✓ Saved to: {output_file}\n")
                processed_count += 1

            except Exception as e:
                print(f"  ✗ Error processing {pdf_path}: {e}\n")

                # Create failure marker
                with open(failed_marker, 'w') as f:
                    f.write(f"Failed with error: {str(e)}\n")

                failed_count += 1
                continue

        # Print summary
        print("\n" + "="*60)
        print(f"Processing Summary:")
        print(f"  ✓ Processed: {processed_count}")
        print(f"  ⊙ Skipped:   {skipped_count}")
        print(f"  ✗ Failed:    {failed_count}")
        print("="*60)

    def process_single_file(self, pdf_path: str, output_path: Optional[str] = None) -> None:
        """
        Process a single PDF file.

        Args:
            pdf_path: Path to the PDF file
            output_path: Optional custom output path
        """
        try:
            markdown_text = self.process_pdf(pdf_path)

            # Determine output path
            if output_path is None:
                pdf_name = Path(pdf_path).stem
                output_path = self.output_dir / f"{pdf_name}.md"

            # Save to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {Path(pdf_path).stem}\n\n")
                f.write(markdown_text)

            print(f"✓ Saved to: {output_path}")

        except Exception as e:
            print(f"✗ Error: {e}")
            sys.exit(1)


def main():
    """Main entry point for the script."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown using Tesseract OCR"
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='PDF file or directory to process (default: current directory)'
    )
    parser.add_argument(
        '-o', '--output-dir',
        default='documents',
        help='Output directory for markdown files (default: documents)'
    )
    parser.add_argument(
        '-d', '--dpi',
        type=int,
        default=300,
        help='DPI for PDF conversion (default: 300)'
    )

    args = parser.parse_args()

    converter = PDFToMarkdownConverter(output_dir=args.output_dir)

    # Process input
    if args.input is None:
        # Process all PDFs in current directory
        converter.process_directory(".", "*.pdf")
    elif os.path.isfile(args.input):
        # Process single file
        converter.process_single_file(args.input)
    elif os.path.isdir(args.input):
        # Process directory
        converter.process_directory(args.input, "*.pdf")
    else:
        print(f"Error: {args.input} is not a valid file or directory")
        sys.exit(1)


if __name__ == "__main__":
    main()
