# CDS Processing Tools

Professional tools for converting Common Data Set files (PDF/Excel) to structured Markdown format.

## Overview

This directory contains Python-based conversion tools designed to extract and structure university Common Data Set data:

| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| `pdf_to_markdown.py` | Convert PDFs with OCR + table extraction | PDF files | Markdown |
| `xls_to_markdown.py` | Convert Excel spreadsheets | XLS/XLSX files | Markdown |
| `automate_cds_pipeline.py` | Batch process with git integration | Mixed files | Markdown + Git |
| `process_all.py` | Simple batch processor | Mixed files | Markdown |
| `run_pipeline.sh` | Shell wrapper for automation | Mixed files | Markdown + Git |

## Quick Start

**Note:** Run these commands from the project root directory.

### Process a Single PDF
```bash
python tools/pdf_to_markdown.py university.pdf
```

### Process a Single Excel File
```bash
python tools/xls_to_markdown.py university.xlsx
```

### Batch Process Directory
```bash
python tools/automate_cds_pipeline.py /path/to/files/
```

## Tool Details

### pdf_to_markdown.py

**Features:**
- Tesseract OCR for text extraction
- PDFPlumber for accurate table extraction
- Multi-page support
- Adjustable DPI quality (300-600)
- Smart skip with `.processed` tracking files
- Progress reporting

**Usage:**
```bash
# Basic usage (outputs to documents/)
python tools/pdf_to_markdown.py input.pdf

# High quality
python tools/pdf_to_markdown.py input.pdf --dpi 600

# Custom output directory
python tools/pdf_to_markdown.py input.pdf -o output_folder/

# Batch process directory
python tools/pdf_to_markdown.py /path/to/pdfs/
```

**Parameters:**
- `input`: PDF file or directory (default: current directory)
- `-o, --output-dir`: Output directory (default: `documents`)
- `--dpi`: DPI for conversion (default: 300, range: 100-600)

### xls_to_markdown.py

**Features:**
- Support for XLS and XLSX formats
- Multi-sheet processing
- Smart table detection
- Preserves formatting
- Skip processed files automatically

**Usage:**
```bash
# Basic usage
python tools/xls_to_markdown.py input.xlsx

# Custom output
python tools/xls_to_markdown.py input.xlsx -o output_folder/

# Batch process
python tools/xls_to_markdown.py /path/to/excel_files/
```

**Parameters:**
- `input`: Excel file or directory (default: current directory)
- `-o, --output-dir`: Output directory (default: `documents`)

### automate_cds_pipeline.py

**Features:**
- Automatic file type detection
- Processes both PDF and Excel
- Git integration (auto-commit)
- Progress tracking
- Error handling and reporting
- Summary statistics

**Usage:**
```bash
# Process directory with git commits
python tools/automate_cds_pipeline.py /path/to/source_files/

# Using shell wrapper
bash tools/run_pipeline.sh /path/to/source_files/
```

**What It Does:**
1. Scans directory for PDF/Excel files
2. Processes each file with appropriate tool
3. Creates `.processed` marker files
4. Stages changes to git
5. Creates descriptive commit message
6. Provides processing summary

### process_all.py

Simple batch processor without git integration.

**Usage:**
```bash
python tools/process_all.py /path/to/files/
```

## Processing Features

### Smart Tracking System

All tools use `.processed` marker files to track processing status:

- **Skip Already Processed**: Automatically skips files with existing `.processed` markers
- **Resume Capability**: Safe to re-run after interruptions
- **Error Tracking**: Creates `.failed` markers for debugging
- **Summary Reports**: Shows Processed/Skipped/Failed counts

Example output:
```
Found 10 PDF file(s)

Processing: Harvard-2024-2025.pdf
  ✓ Saved to: documents/Harvard-2024-2025.md

⊙ Skipping Yale-2024-2025.pdf (already processed)

============================================================
Processing Summary:
  ✓ Processed: 1
  ⊙ Skipped:   9
  ✗ Failed:    0
============================================================
```

### Table Extraction

PDF processing includes professional table extraction:

- Uses `pdfplumber` library for accurate table detection
- Preserves column alignment and cell content
- Properly formats markdown tables
- Handles merged cells and complex layouts

**Example**: Admissions Factors Table (Section C7)

Before (OCR only):
```
Academic | Very Important | Important |Considered| Not
Rigor    |                |    X      |          |
GPA      |                |    X      |          |
```

After (with table extraction):
```
| Academic                     | Very Important | Important | Considered | Not |
| ---------------------------- | -------------- | --------- | ---------- | --- |
| Rigor of secondary school    |                |           | X          |     |
| Academic GPA                 |                |           | X          |     |
```

## Requirements

### Python Dependencies

Install all dependencies:
```bash
pip install -r ../requirements.txt
```

Or individually:
```bash
pip install pytesseract Pillow pdf2image pdfplumber camelot-py openpyxl xlrd
```

### System Dependencies

**macOS:**
```bash
brew install tesseract poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr poppler-utils
```

## Output Structure

All tools output to the `documents/` directory by default:

```
documents/
├── Harvard-2024-2025.md
├── Yale-2024-2025.md
├── MIT-2024-2025.md
├── .Harvard-2024-2025.processed
├── .Yale-2024-2025.processed
└── .MIT-2024-2025.processed
```

## Troubleshooting

### Common Issues

**1. "tesseract is not installed"**
```bash
# macOS
brew install tesseract

# Ubuntu/Debian
sudo apt-get install tesseract-ocr
```

**2. "Unable to load PDF"**
```bash
# macOS
brew install poppler

# Ubuntu/Debian
sudo apt-get install poppler-utils
```

**3. Poor OCR Quality**

Increase DPI:
```bash
python pdf_to_markdown.py file.pdf --dpi 600
```

**4. Memory Issues**

Process files one at a time instead of batch:
```bash
python pdf_to_markdown.py single_file.pdf
```

**5. Table Extraction Errors**

Check that pdfplumber is installed:
```bash
pip install pdfplumber camelot-py[cv]
```

### Debug Mode

For detailed error information, check the `.failed` marker files in the output directory.

## Performance Tips

1. **Batch Processing**: Process multiple files in one run
2. **DPI Balance**: Use 300 DPI for speed, 600 DPI for quality
3. **SSD Storage**: Use SSD for faster image processing
4. **Parallel Processing**: Run multiple instances on different directories

## Advanced Usage

### Custom Processing Pipeline

```python
from pdf_to_markdown import PDFToMarkdownConverter

converter = PDFToMarkdownConverter(output_dir="custom_output")
converter.process_pdf("university.pdf", dpi=600)
```

### Programmatic Access

```python
from xls_to_markdown import ExcelToMarkdownConverter

converter = ExcelToMarkdownConverter(output_dir="output")
converter.process_file("university.xlsx")
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for detailed contribution guidelines.

## Support

For issues or questions:
1. Check this README
2. Review [CONTRIBUTING.md](../CONTRIBUTING.md)
3. Open an issue on GitHub

## License

MIT License - See LICENSE file for details
