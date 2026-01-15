---
name: xls-to-md
description: Convert Excel files (XLS/XLSX) to Markdown format. Use when the user wants to convert Excel spreadsheets to markdown, process Common Data Set Excel files from universities like UIUC, or extract tabular data from Excel workbooks.
allowed-tools: Read, Bash, Write, Glob
---

# Excel to Markdown Converter Skill

## What this Skill does

Converts Excel files (.xls, .xlsx, .xlsm) to Markdown format. This skill:
- Extracts data from Excel workbooks directly (no OCR needed)
- Processes all sheets in the workbook
- Intelligently detects tables, headers, and data structures
- Formats output as clean markdown tables
- Preserves data accuracy and structure

## When to use this skill

Use this skill when you need to:
- Convert university Common Data Set Excel files (like UIUC, Purdue, Michigan)
- Extract tables from Excel spreadsheets into markdown
- Process structured data from .xls or .xlsx files
- Convert Excel reports to markdown format

## Quick start

### Process a single Excel file:
```bash
python tools/xls_to_markdown.py university.xlsx
```

### Process all Excel files in a directory:
```bash
python tools/xls_to_markdown.py /path/to/excel/files/
```

### Custom output directory:
```bash
python tools/xls_to_markdown.py university.xlsx -o markdown_output/
```

## Usage examples

**Example 1: Convert UIUC Common Data Set**
```bash
python tools/xls_to_markdown.py UIUC_CDS_2024.xlsx
# Output: documents/UIUC_CDS_2024.md
```

**Example 2: Batch convert all Excel files**
```bash
python tools/xls_to_markdown.py ./downloads/ -o converted/
```

**Example 3: Process current directory**
```bash
python tools/xls_to_markdown.py .
# Processes all Excel files in current directory
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `input` | Excel file or directory to process | Current directory |
| `-o, --output-dir` | Output directory for markdown files | `documents` |

## Requirements

### Python packages:
```bash
pip install openpyxl xlrd
```

No system dependencies required (unlike PDF processing).

## Supported formats

- `.xls` - Excel 97-2003 format
- `.xlsx` - Excel 2007+ format
- `.xlsm` - Excel with macros

## Features

- **Multi-sheet support**: Processes all worksheets in the workbook
- **Intelligent parsing**:
  - Automatically detects tables and formats as markdown tables
  - Identifies section headers and creates proper heading hierarchy
  - Recognizes key-value pairs
  - Detects and formats lists
- **Data type handling**:
  - Preserves numbers, text, and boolean values
  - Converts checkboxes to ✓ symbols
  - Maintains table structure and alignment
- **Fast and accurate**: Direct data extraction (no OCR)

## Output format

Generated markdown includes:
- University name as H1 header (from filename)
- Sheet names as H2 headers
- Subsections as H3/H4 headers
- Tables with proper markdown formatting
- Key-value pairs formatted as tables
- Lists with bullet points

## How it works

The converter analyzes each Excel sheet and:

1. **Detects Section Headers**: Rows with a single cell are treated as headers
2. **Identifies Tables**: Consecutive rows with multiple columns become markdown tables
3. **Recognizes Patterns**:
   - Two-column data → Key-value pairs
   - Single-column data → List items
   - Multi-column data → Tables
4. **Formats Markdown**:
   - Creates proper heading hierarchy
   - Generates markdown tables with headers
   - Preserves data types and formatting

## Tips for best results

### Excel File Organization

For optimal conversion, organize your Excel file with:
- **Clear Headers**: Use merged cells or single-column rows for section headers
- **Consistent Tables**: Keep table structures uniform (same number of columns)
- **Proper Sheets**: Separate major sections into different sheets
- **Descriptive Sheet Names**: Name sheets clearly (e.g., "Section A", "Enrollment Data")

## Advantages over PDF conversion

| Feature | Excel Converter | PDF Converter |
|---------|----------------|---------------|
| Accuracy | Very High (direct data) | Depends on OCR quality |
| Speed | Fast | Slower (requires OCR) |
| Structure | Preserved perfectly | Detected heuristically |
| Dependencies | Just Python packages | Requires Tesseract + Poppler |

**Use Excel converter whenever Excel format is available.**

## Troubleshooting

### "No module named 'openpyxl'"
Install the required packages:
```bash
pip install openpyxl xlrd
```

### Tables not formatting correctly
Ensure table rows have consistent column counts. Merged cells may cause issues.

### Missing data
Check if the Excel file has:
- Password protection (not supported)
- Hidden sheets (only visible sheets are processed)

### Encoding issues
The tool outputs UTF-8 encoded files. Ensure your text editor supports UTF-8.

## Related skills

- **pdf-to-md**: For converting PDF files to markdown
- **cds-pipeline**: For full automation with git integration

## Documentation

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for complete processing guide and [tools/README.md](../../tools/README.md) for detailed tool documentation.
