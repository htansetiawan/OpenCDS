---
name: pdf-to-md
description: Convert PDF files to Markdown using OCR. Use when the user wants to convert PDF documents to markdown format, extract text from PDFs, process Common Data Set PDFs, or digitize scanned documents.
allowed-tools: Read, Bash, Write, Glob
---

# PDF to Markdown Converter Skill

## What this Skill does

Converts PDF files to Markdown format using Tesseract OCR. This skill:
- Extracts text from PDF documents using OCR
- Handles multi-page PDFs
- Formats output as clean markdown with headers and structure
- Supports quality adjustment via DPI settings

## When to use this skill

Use this skill when you need to:
- Convert university Common Data Set PDFs to markdown
- Extract text from PDF documents
- Process scanned PDF files
- Digitize PDF reports into markdown format

## Quick start

### Process a single PDF file:
```bash
python tools/pdf_to_markdown.py document.pdf
```

### Process all PDFs in a directory:
```bash
python tools/pdf_to_markdown.py /path/to/pdfs/
```

### High-quality OCR (slower but more accurate):
```bash
python tools/pdf_to_markdown.py document.pdf --dpi 600
```

### Custom output directory:
```bash
python tools/pdf_to_markdown.py document.pdf -o markdown_output/
```

## Usage examples

**Example 1: Convert a university CDS PDF**
```bash
python tools/pdf_to_markdown.py Harvard_CDS_2024.pdf
# Output: documents/Harvard_CDS_2024.md
```

**Example 2: Batch convert all PDFs with high quality**
```bash
python tools/pdf_to_markdown.py ./downloads/ --dpi 600 -o converted/
```

**Example 3: Process current directory**
```bash
python tools/pdf_to_markdown.py .
# Processes all PDFs in current directory
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `input` | PDF file or directory to process | Current directory |
| `-o, --output-dir` | Output directory for markdown files | `documents` |
| `--dpi` | DPI for PDF conversion (higher = better quality) | `300` |

## Requirements

### Python packages:
```bash
pip install pytesseract Pillow pdf2image
```

### System dependencies:

**macOS:**
```bash
brew install tesseract poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr poppler-utils
```

## Features

- **Multi-page support**: Automatically processes all pages in a PDF
- **Auto-formatting**: Detects headers and formats markdown structure
- **Quality control**: Adjustable DPI for accuracy vs. speed tradeoff
- **Batch processing**: Process entire directories of PDFs
- **Progress tracking**: Shows real-time progress for each file

## Output format

Generated markdown includes:
- Document title as H1 header
- Page numbers as H2 headers (for multi-page docs)
- Auto-detected section headers
- Clean paragraph formatting
- Proper table extraction

## Tips for best results

1. **Use higher DPI for important documents**: `--dpi 600` for official documents
2. **Check source PDF quality**: Better source = better OCR results
3. **Review output**: OCR may have errors, always verify critical data
4. **Batch similar files**: Process files of similar quality together

## Troubleshooting

### "tesseract is not installed"
Install Tesseract OCR:
```bash
brew install tesseract  # macOS
sudo apt-get install tesseract-ocr  # Ubuntu
```

### "Unable to load PDF"
Install poppler-utils:
```bash
brew install poppler  # macOS
sudo apt-get install poppler-utils  # Ubuntu
```

### Poor OCR quality
Try increasing DPI:
```bash
python tools/pdf_to_markdown.py document.pdf --dpi 600
```

### Memory issues with large PDFs
Process one file at a time instead of batch processing.

## Related skills

- **xls-to-md**: For converting Excel files to markdown
- **cds-pipeline**: For full automation with git integration

## Documentation

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for complete processing guide and [tools/README.md](../../tools/README.md) for detailed tool documentation.
