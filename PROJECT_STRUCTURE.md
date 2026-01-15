# OpenCDS Project Structure

```
OpenCDS/
├── README.md                    # Main project documentation
├── CONTRIBUTING.md              # Contribution guidelines and processing guide
├── LICENSE                      # MIT License
├── requirements.txt             # Python dependencies
│
├── documents/                   # Converted CDS markdown files (30 universities)
│   ├── Harvard-2024-2025.md
│   ├── Yale-2024-2025.md
│   ├── MIT-2024-2025.md
│   └── ...
│
└── tools/                       # Processing tools
    ├── README.md                # Tools documentation
    ├── pdf_to_markdown.py       # PDF → Markdown converter
    ├── xls_to_markdown.py       # Excel → Markdown converter
    ├── automate_cds_pipeline.py # Automated batch processor
    ├── process_all.py           # Simple batch processor
    └── run_pipeline.sh          # Shell wrapper
```

## Directory Descriptions

### Root Files
- **README.md**: Main project overview, university list, and quick start guide
- **CONTRIBUTING.md**: Comprehensive guide for contributors and tool usage
- **requirements.txt**: All Python dependencies for the processing tools
- **LICENSE**: MIT License for the project

### documents/
Contains all converted Common Data Set files in Markdown format. One file per university.

**Naming convention:** `University-YYYY-YYYY.md` (e.g., `Harvard-2024-2025.md`, `MIT-2025-2026.md`)

**Current Dataset:** 2024-2025 academic year

**Contents:**
- Structured CDS sections (A-J)
- Properly formatted tables
- Complete institutional data
- OCR-extracted text

**Note:** Tools support any academic year - contributions for newer years welcome!

### tools/
Python scripts and utilities for processing CDS files.

**Main Scripts:**
- `pdf_to_markdown.py`: Professional PDF converter with OCR and table extraction
- `xls_to_markdown.py`: Excel file converter with multi-sheet support
- `automate_cds_pipeline.py`: Full automation with git integration
- `process_all.py`: Simple batch processor
- `run_pipeline.sh`: Shell wrapper for easy execution

**Features:**
- Progress tracking with `.processed` files
- Smart skip (don't reprocess completed files)
- Error handling with `.failed` markers
- Summary statistics

## File Counts

- **CDS Files**: 30 universities
- **Python Tools**: 4 scripts
- **Documentation**: 3 markdown files (README, CONTRIBUTING, PROJECT_STRUCTURE)
- **Total LOC**: ~2,500 lines of Python code

## Usage Patterns

### For Users (Reading Data)
```
documents/ → Browse CDS files
README.md  → Find university links
```

### For Contributors (Processing Files)
```
tools/README.md     → Learn about tools
CONTRIBUTING.md     → Follow processing guidelines
tools/*.py          → Run conversion scripts
```

### For Developers (Extending Tools)
```
tools/              → View source code
CONTRIBUTING.md     → Understand architecture
tools/README.md     → Tool implementation details
```
