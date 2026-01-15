# OpenCDS

> **Open, structured, machine-readable university Common Data Set repository**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CDS Year](https://img.shields.io/badge/CDS-2024--2025-blue.svg)](documents/)

## Overview

**OpenCDS** is an open-source repository that transforms university Common Data Set (CDS) reports into structured, machine-readable Markdown format. The project provides both the converted data and professional tools to process CDS files from any year.

**Current Dataset:** CDS 2024-2025 from 30 top universities, including critical admissions statistics, enrollment numbers, test scores, and institutional information.

### What's Included

- **Current Dataset (2024-2025)**: 30 top universities (Ivy League, top private, flagship public)
- **Structured Format**: Clean Markdown with properly formatted tables
- **Complete Sections**: All CDS sections (A-J) including admissions, enrollment, financial aid
- **Processing Tools**: Professional Python tools for converting CDS files from any year
- **Accurate Tables**: Advanced extraction preserves column alignment and data structure

### Quick Links

- 📄 [Browse Data](documents/) - View converted CDS files (2024-2025)
- 🛠️ [Processing Tools](tools/) - Convert your own CDS files (any year)
- 🤝 [Contributing](CONTRIBUTING.md) - Add universities or update to newer years

## Current Dataset (2024-2025)

The following universities are currently included in this repository. The tools can process CDS files from any year - contributions for newer academic years are welcome!

### Ivy League + Top Private

| University | File | Official Source |
|------------|------|-----------------|
| Harvard | [Harvard-2024-2025.md](documents/Harvard-2024-2025.md) | [OIRA](https://oira.harvard.edu/common-data-set/) |
| Yale | [Yale-2024-2025.md](documents/Yale-2024-2025.md) | [OIR](https://oir.yale.edu/common-data-set) |
| Princeton | [Princeton-2024-2025.md](documents/Princeton-2024-2025.md) | [IR](https://ir.princeton.edu/other-university-data/common-data-set) |
| MIT | [MIT-2024-2025.md](documents/MIT-2024-2025.md) | [IR](https://ir.mit.edu/) |
| Stanford | [Stanford-2024-2025.md](documents/Stanford-2024-2025.md) | [IRDS](https://irds.stanford.edu/data-findings/cds) |
| Columbia | [Columbia-2024-2025.md](documents/Columbia-2024-2025.md) | [OPIR](https://opir.columbia.edu/understanding-columbias-common-data-set) |
| UPenn | [UPenn-2024-2025.md](documents/UPenn-2024-2025.md) | [IRA](https://ira.upenn.edu/penn-numbers/common-data-set) |
| Cornell | [Cornell-2024-2025.md](documents/Cornell-2024-2025.md) | [IRP](https://irp.dpb.cornell.edu/common-data-set) |
| Brown | [Brown-2024-2025.md](documents/Brown-2024-2025.md) | [OIR](https://oir.brown.edu/institutional-data/common-data-set) |
| Dartmouth | [Darmouth-2024-2025.md](documents/Darmouth-2024-2025.md) | [OIR](https://www.dartmouth.edu/oir/data-reporting/cds/) |
| Caltech | [Caltech-2024-2025.md](documents/Caltech-2024-2025.md) | [IRO](https://iro.caltech.edu/data) |
| Duke | [Duke-2024-2025.md](documents/Duke-2024-2025.md) | [OIR](https://ir.provost.duke.edu/facts-figures/common-data-sets/) |
| UChicago | [UChicago-2024-2025.md](documents/UChicago-2024-2025.md) | [Registrar](https://data.uchicago.edu/common-data-set/) |
| Northwestern | [Northwestern-2024-2025.md](documents/Northwestern-2024-2025.md) | [Enrollment](https://www.enrollment.northwestern.edu/data/common-data-set.html) |
| Johns Hopkins | [JHU-2024-2025.md](documents/JHU-2024-2025.md) | [OIRA](https://oira.jhu.edu/reports-2/) |
| Vanderbilt | [Vanderbilt-2024-2025.md](documents/Vanderbilt-2024-2025.md) | [IRA](https://www.vanderbilt.edu/data/public-data/common-data-sets/) |
| Rice | [RICE-2024-2025.md](documents/RICE-2024-2025.md) | [OIE](https://ideas.rice.edu/reporting-analytics/common-data-set/) |
| CMU | [CMU-2024-2025.md](documents/CMU-2024-2025.md) | - |
| NYU | [NYU-2024-2025.md](documents/NYU-2024-2025.md) | - |
| USC | [USC-2024-2025.md](documents/USC-2024-2025.md) | [OIR](https://oir.usc.edu/common-data-set/) |

### Top Public Universities

| University | File | Official Source |
|------------|------|-----------------|
| UC Berkeley | [UCBerkeley-2024-2025.md](documents/UCBerkeley-2024-2025.md) | [OPA](https://opa.berkeley.edu/campus-data/common-data-set) |
| UCLA | [UCLA-2024-2025.md](documents/UCLA-2024-2025.md) | [APB](https://apb.ucla.edu/campus-statistics/common-data-set-undergraduate-profile) |
| UMich Ann Arbor | [UMich-2024-2025.md](documents/UMich-2024-2025.md) | [OBP](https://obp.umich.edu/campus-statistics/common-data-set/) |
| UW Seattle | [UWSeattle-2024-2025.md](documents/UWSeattle-2024-2025.md) | [OPB](https://www.washington.edu/opb/uw-data/external-reporting/common-data-set/) |
| UCSD | [UCSD-2024-2025.md](documents/UCSD-2024-2025.md) | [IR](https://ir.ucsd.edu/stats/undergrad/common-data-set.html) |
| Georgia Tech | [GATech-2024-2025.md](documents/GATech-2024-2025.md) | [IRP](https://irp.gatech.edu/common-data-set) |
| UIUC | [UIUC-2024-2025.md](documents/UIUC-2024-2025.md) | [DMI](https://www.dmi.illinois.edu/stuenr/) |
| UW Madison | [UWisconsin-2024-2025.md](documents/UWisconsin-2024-2025.md) | [DAPIR](https://data.wisc.edu/common-data-set-and-rankings/) |
| UT Austin | [UTAustin-2024-2025.md](documents/UTAustin-2024-2025.md) | [IRRIS](https://reports.utexas.edu/common-data-set) |
| Purdue | [Purdue-2024-2025.md](documents/Purdue-2024-2025.md) | [Data Analytics](https://www.purdue.edu/idata/data/common-data-set/) |

## Features

### 🎯 Accessible Data

- **Machine-Readable**: Structured Markdown format for easy parsing
- **Searchable**: Text-based format enables full-text search
- **Portable**: Works with any text editor or markdown viewer
- **Version Controlled**: Track changes over time with git

### 📊 Accurate Tables

Professional table extraction ensures:
- Proper column alignment
- Preserved data structure
- Accurate admissions factors (Section C7)
- Correct test score percentiles (Section C9)

### 🔧 Processing Tools

Professional Python tools for converting your own CDS files:
- PDF to Markdown with OCR + table extraction
- Excel to Markdown with sheet processing
- Batch automation with progress tracking
- See [tools/](tools/) directory

## Usage

### Browsing Data

All converted files are in the [documents/](documents/) directory:

```bash
# Clone the repository
git clone https://github.com/yourusername/OpenCDS.git
cd OpenCDS

# Browse a specific university (current: 2024-2025)
cat documents/Harvard-2024-2025.md

# Search across all files
grep -r "SAT Math" documents/
```

### Processing Your Own Files

**The tools work for CDS files from any academic year.** Simply download the CDS PDF/Excel from a university and run:

```bash
# Install dependencies (one-time setup)
pip install -r requirements.txt
brew install tesseract poppler  # macOS

# Convert a PDF (any year)
python tools/pdf_to_markdown.py university_cds_2025_2026.pdf

# Convert an Excel file (any year)
python tools/xls_to_markdown.py university_cds_2023_2024.xlsx

# Batch process directory
python tools/automate_cds_pipeline.py /path/to/files/
```

See [tools/README.md](tools/README.md) for detailed usage.

## Data Structure

Each CDS markdown file contains:

### Section Breakdown
- **A**: General Information
- **B**: Enrollment and Persistence
- **C**: First-Time, First-Year Admission
- **D**: Transfer Admission
- **E**: Academic Offerings and Policies
- **F**: Student Life
- **G**: Annual Expenses
- **H**: Financial Aid
- **I**: Instructional Faculty and Class Size
- **J**: Degrees Conferred

### Key Data Points
- Acceptance rates and application numbers
- Test score ranges (SAT/ACT)
- GPA requirements and class rank
- Enrollment statistics by demographics
- Financial aid statistics
- Faculty information

## Disclaimer

⚠️ **Important**: This data is provided "AS IS" without warranty.

- **Potential for Errors**: AI OCR extraction may introduce errors
- **Not Official**: We are not affiliated with these universities
- **Verify Critical Data**: Always check official sources for decisions
- **Use Responsibly**: For research and preliminary analysis only

**Always verify against official sources** before making academic, financial, or personal decisions.

## Methodology

### Data Extraction

1. **Source Collection**: Official CDS PDFs/Excel from university websites
2. **AI OCR Processing**: Tesseract OCR with pdfplumber for tables
3. **Structured Formatting**: Automated conversion to Markdown
4. **Quality Control**: Manual verification of critical sections
5. **Version Control**: Git tracking for transparency

### Quality Assurance

- Advanced table extraction preserves column alignment
- Multiple validation passes on admissions data
- Comparison against official sources
- Community review and error reporting

## Contributing

We welcome contributions! You can help by:

- **Adding universities**: Convert CDS files for new institutions (any year)
- **Updating to newer years**: Process 2025-2026, 2026-2027, etc. when available
- **Fixing errors**: Report or fix OCR mistakes
- **Improving tools**: Enhance processing scripts
- **Documentation**: Improve guides and examples

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Credits

The [Common Data Set Initiative](https://commondataset.org/) is a collaborative effort by:
- **The College Board**
- **Peterson's**
- **U.S. News & World Report**

All data is intellectual property of respective institutions.

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Support

- 🐛 [Issues](https://github.com/yourusername/OpenCDS/issues) - Report bugs
- 💬 [Discussions](https://github.com/yourusername/OpenCDS/discussions) - Ask questions
- 🌟 [Star this repo](https://github.com/yourusername/OpenCDS) - Show your support!

---

**OpenCDS** - Making university admissions data accessible to everyone
*Built with ❤️ for students, researchers, and education data enthusiasts*
