# Contributing to OpenCDS

Thank you for your interest in contributing to OpenCDS! This guide will help you process CDS files from any academic year and contribute to the repository.

**Note:** While the current dataset contains CDS 2024-2025 files, the tools and processes work for **any academic year**. Contributions for newer years (2025-2026, 2026-2027, etc.) are especially welcome!

## Table of Contents

- [Quick Start](#quick-start)
- [Processing Tools](#processing-tools)
- [PDF Processing](#pdf-processing)
- [Excel Processing](#excel-processing)
- [Automated Pipeline](#automated-pipeline)
- [Requirements](#requirements)
- [Verification Guidelines](#verification-guidelines)

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OpenCDS.git
cd OpenCDS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install system dependencies (macOS):
```bash
brew install tesseract poppler
```

For Ubuntu/Debian:
```bash
sudo apt-get install tesseract-ocr poppler-utils
```

## Processing Tools

All processing tools are located in the `tools/` directory. The repository provides three main processing scripts:

### 1. PDF to Markdown (`pdf_to_markdown.py`)

Converts PDF files to Markdown format using OCR and advanced table extraction.

**Single file:**
```bash
python tools/pdf_to_markdown.py university_cds.pdf
```

**Batch process directory:**
```bash
python tools/pdf_to_markdown.py /path/to/pdfs/
```

**High-quality OCR:**
```bash
python tools/pdf_to_markdown.py document.pdf --dpi 600
```

**Custom output:**
```bash
python tools/pdf_to_markdown.py document.pdf -o custom_output/
```

### 2. Excel to Markdown (`xls_to_markdown.py`)

Converts Excel files (XLS/XLSX) to Markdown format.

**Single file:**
```bash
python tools/xls_to_markdown.py university_cds.xlsx
```

**Batch process:**
```bash
python tools/xls_to_markdown.py /path/to/excel_files/
```

### 3. Automated Pipeline (`automate_cds_pipeline.py`)

Full automation with git integration for batch processing.

```bash
python tools/automate_cds_pipeline.py /path/to/source_files/
```

## PDF Processing

### Features

- **OCR Text Extraction**: Uses Tesseract OCR for accurate text extraction
- **Advanced Table Detection**: Employs `pdfplumber` for professional table extraction
- **Multi-page Support**: Processes all pages automatically
- **Quality Control**: Adjustable DPI (300-600) for accuracy vs. speed
- **Progress Tracking**: `.processed` files prevent redundant processing

### Usage Examples

**Process a university CDS PDF:**
```bash
python tools/pdf_to_markdown.py Harvard_CDS_2024.pdf
# Output: documents/Harvard_CDS_2024.md
```

**Batch convert with high quality:**
```bash
python tools/pdf_to_markdown.py ./downloads/ --dpi 600 -o converted/
```

### Output Format

Generated markdown includes:
- Document title as H1 header
- Page numbers as H2 headers (for multi-page docs)
- Auto-detected section headers
- Clean paragraph formatting
- Properly formatted tables with accurate column alignment

### Tips for Best Results

1. **Use higher DPI for important documents**: `--dpi 600` for official documents
2. **Check source PDF quality**: Better source = better OCR results
3. **Review output**: OCR may have errors, always verify critical data
4. **Batch similar files**: Process files of similar quality together

### Troubleshooting

**"tesseract is not installed"**
```bash
brew install tesseract  # macOS
sudo apt-get install tesseract-ocr  # Ubuntu
```

**"Unable to load PDF"**
```bash
brew install poppler  # macOS
sudo apt-get install poppler-utils  # Ubuntu
```

**Poor OCR quality**
```bash
python tools/pdf_to_markdown.py document.pdf --dpi 600
```

## Excel Processing

### Features

- **Multi-sheet Support**: Processes all sheets in workbook
- **Smart Formatting**: Auto-detects tables, headers, and key-value pairs
- **Format Preservation**: Maintains cell formatting and structure
- **Both XLS and XLSX**: Supports legacy and modern Excel formats

### Usage Examples

**Process a CDS Excel file:**
```bash
python tools/xls_to_markdown.py UIUC_CDS_2024.xlsx
# Output: documents/UIUC_CDS_2024.md
```

**Batch process directory:**
```bash
python tools/xls_to_markdown.py /path/to/excel_files/
```

### Output Format

- Each sheet becomes a section (## Sheet Name)
- Tables are formatted as markdown tables
- Key-value pairs formatted as definition lists
- Empty cells handled gracefully

## Automated Pipeline

The automated pipeline combines both PDF and Excel processing with git integration.

### Features

- Processes both PDF and Excel files
- Automatic git commits with descriptive messages
- Progress tracking with `.processed` files
- Error handling and retry logic
- Summary statistics

### Usage

```bash
# Process files from a directory
python tools/automate_cds_pipeline.py /Users/Downloads/CDS/

# Or use the shell script wrapper
bash tools/run_pipeline.sh /Users/Downloads/CDS/
```

### What It Does

1. Scans directory for PDF and Excel files
2. Processes each file with appropriate converter
3. Tracks processing status with marker files
4. Commits results to git with detailed commit messages
5. Provides summary report

## Requirements

### Python Packages

```
# PDF Processing
pytesseract>=0.3.10
Pillow>=10.0.0
pdf2image>=1.16.0

# Table Extraction (recommended)
pdfplumber>=0.10.0
camelot-py[cv]>=0.11.0

# Excel Processing
openpyxl>=3.1.0
xlrd>=2.0.1
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

## Verification Guidelines

### Data Accuracy

After processing, please verify:

1. **Table Structure**: Check that tables maintain proper column alignment
2. **Critical Numbers**: Verify enrollment numbers, test scores, percentages
3. **Section Headers**: Ensure all CDS sections (A-J) are present
4. **Special Characters**: Check for OCR errors with symbols and punctuation

### Quality Checklist

- [ ] All pages processed successfully
- [ ] Tables are properly formatted
- [ ] No obvious OCR errors in critical data
- [ ] File named correctly (University-YYYY-YYYY.md)
- [ ] Committed to correct location (documents/)

### Reporting Errors

If you find errors in the converted data:

1. Open an issue describing the error
2. Include the university name and section
3. Provide the correct value from the official source
4. Link to the official CDS document

## Adding New Universities

1. Download the official CDS document
2. Process using appropriate tool
3. Review output for accuracy
4. Add official source link to README.md
5. Commit with message: "Add [University] CDS 2024-2025"

## Best Practices

1. **Always verify against official sources**
2. **Process one university at a time for first-time contributions**
3. **Use high DPI (600) for scanned PDFs**
4. **Review admissions factors tables carefully** (Section C7)
5. **Check test score percentiles** (Section C9)
6. **Maintain consistent naming**: `University-2024-2025.md`

## Getting Help

- Review issues for similar problems
- Check [tools/README.md](tools/README.md) for tool documentation
- Open a new issue with details and error messages

## License

By contributing, you agree that your contributions will be licensed under the same license as this project.
