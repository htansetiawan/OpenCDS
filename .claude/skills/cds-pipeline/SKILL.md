---
name: cds-pipeline
description: Automated end-to-end pipeline for processing Common Data Set files and pushing to git. Use when the user wants to process multiple PDF and Excel files, automate the entire workflow, commit and push changes to git, or batch process university data files.
allowed-tools: Read, Bash, Write, Glob, Grep
---

# Common Data Set Automation Pipeline Skill

## What this Skill does

Complete end-to-end automation pipeline that:
1. ✓ Processes all PDF files using OCR
2. ✓ Processes all Excel files
3. ✓ Converts everything to markdown
4. ✓ Stages files in git
5. ✓ Creates commit with timestamp
6. ✓ Pushes to remote repository

## When to use this skill

Use this skill when you need to:
- Process an entire folder of Common Data Set files (mixed PDFs and Excel)
- Automate the complete workflow from source files to git repository
- Batch process multiple universities at once
- Set up automated data collection workflows
- Push processed files to a specific git repository

## Quick start

### Process files and commit to current repository:
```bash
python tools/automate_cds_pipeline.py ./raw_files
```

### Process and push to specific git repository:
```bash
python tools/automate_cds_pipeline.py ./raw_files \
  --git-url https://github.com/user/repo.git
```

### High-quality PDF processing:
```bash
python tools/automate_cds_pipeline.py ./raw_files --dpi 600
```

### Process files only (skip git operations):
```bash
python tools/automate_cds_pipeline.py ./raw_files --skip-git
```

## Usage examples

**Example 1: Batch process new universities**
```bash
# Download CDS files to raw_files/
# Then run:
python tools/automate_cds_pipeline.py raw_files
```

**Example 2: Process with specific repository**
```bash
python tools/automate_cds_pipeline.py ./downloads \
  --git-url git@github.com:username/cds-collection.git \
  --dpi 600
```

**Example 3: Review before committing**
```bash
# Process first
python tools/automate_cds_pipeline.py ./files --skip-git
# Review documents/
# Then manually commit or use /commit skill
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `input_folder` | Folder with PDF and Excel files | Required |
| `-o, --output-folder` | Output directory for markdown | `documents` |
| `--git-url` | Git repository URL to push to | None (uses current repo) |
| `--dpi` | DPI for PDF conversion | `300` |
| `--skip-git` | Skip git operations | `false` |

## Requirements

### Python packages:
```bash
pip install -r requirements.txt
```

This installs:
- pytesseract, Pillow, pdf2image (for PDF processing)
- openpyxl, xlrd (for Excel processing)

### System dependencies:

**macOS:**
```bash
brew install tesseract poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install tesseract-ocr poppler-utils
```

## What the pipeline does

### Step 1: Process Excel files
- Finds all `.xls`, `.xlsx`, `.xlsm` files
- Converts each to markdown
- Preserves table structure perfectly
- Fast and accurate (no OCR)

### Step 2: Process PDF files
- Finds all `.pdf` files
- Uses Tesseract OCR to extract text
- Converts to markdown with formatting
- Adjustable quality via DPI

### Step 3: Git operations (optional)
- Stages all output files
- Creates commit with structured message:
  ```
  Add Common Data Set markdown files

  Processed on: 2024-01-14 15:30:45
  Source folder: raw_files

  Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
  ```
- Pushes to remote repository

## Pipeline output

The pipeline provides detailed progress:
```
======================================================================
COMMON DATA SET AUTOMATION PIPELINE
======================================================================
Input folder:  /path/to/raw_files
Output folder: /path/to/output
======================================================================

STEP 1: Processing Excel files...
----------------------------------------------------------------------
  Found 2 Excel file(s)

  Processing: UIUC.xlsx
  ✓ Saved to: output/UIUC.md

  Processing: Purdue.xlsx
  ✓ Saved to: output/Purdue.md
  ✓ Processed 2 Excel file(s)

STEP 2: Processing PDF files...
----------------------------------------------------------------------
  Found 3 PDF file(s)
  Using DPI: 300

  Processing: Harvard.pdf
  ✓ Saved to: output/Harvard.md

  Processing: MIT.pdf
  ✓ Saved to: output/MIT.md

  Processing: Stanford.pdf
  ✓ Saved to: output/Stanford.md
  ✓ Processed 3 PDF file(s)

STEP 3: Git operations...
----------------------------------------------------------------------
  Staging files...
  Creating commit...
  Pushing to remote...
  ✓ Changes committed and pushed successfully

======================================================================
PIPELINE SUMMARY
======================================================================
Excel processing:  ✓ Success
PDF processing:    ✓ Success
Git operations:    ✓ Success
======================================================================

🎉 Pipeline completed successfully!
```

## Workflow options

### Option 1: Fully Automated (Default)
One command does everything:
```bash
python tools/automate_cds_pipeline.py ./raw_files
```

**Pros:**
- Fastest workflow
- Consistent commit messages
- Great for batch processing

**Cons:**
- Less control over commits
- Can't review before pushing

### Option 2: Manual Review
Process first, then review:
```bash
# Step 1: Process
python tools/automate_cds_pipeline.py ./raw_files --skip-git

# Step 2: Review documents/ files

# Step 3: Commit using Claude's /commit skill
# Or manually: git add documents/ && git commit && git push
```

**Pros:**
- Review changes before committing
- Custom commit messages
- More control

**Cons:**
- Two-step process
- Need manual intervention

## Integration with Claude /commit skill

For manual git control with AI assistance:

```bash
# Process files only
python tools/automate_cds_pipeline.py ./raw_files --skip-git
```

Then use Claude's `/commit` skill to create an AI-generated commit message.

## Directory structure recommendation

```
project/
├── raw_files/          # Input files (gitignored)
│   ├── UIUC.xlsx
│   ├── Harvard.pdf
│   └── MIT.pdf
└── documents/          # Generated markdown (committed)
    ├── UIUC.md
    ├── Harvard.md
    └── MIT.md
```

## Tips for best results

1. **Organize source files**: Put all PDFs and Excel files in one folder
2. **Use descriptive filenames**: University name helps generate better markdown
3. **Start with --skip-git**: Test conversions before committing
4. **Use high DPI for official docs**: `--dpi 600` for important documents
5. **Keep raw files**: Don't delete source files after processing

## Troubleshooting

### "Not a git repository"
Either:
- Initialize git: `git init && git remote add origin <url>`
- Provide git URL: `--git-url <url>`
- Skip git: `--skip-git`

### "Excel/PDF processing dependencies not installed"
Install required packages:
```bash
pip install -r requirements.txt
brew install tesseract poppler  # macOS
```

### "Permission denied" on git push
Setup SSH keys or use HTTPS with credentials:
```bash
python tools/automate_cds_pipeline.py ./input \
  --git-url git@github.com:user/repo.git
```

## Related skills

- **pdf-to-md**: For processing individual PDF files
- **xls-to-md**: For processing individual Excel files

## Use this skill vs. individual skills

| Scenario | Use This Skill | Use Individual Skills |
|----------|----------------|----------------------|
| Batch processing | ✓ | |
| Mixed file types | ✓ | |
| Automated workflow | ✓ | |
| Single file | | ✓ |
| Testing conversion | | ✓ |
| Custom workflow | | ✓ |

## Documentation

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for complete processing guide and [tools/README.md](../../tools/README.md) for detailed tool documentation.

## Simple shell wrapper

For convenience, also available as:
```bash
bash tools/run_pipeline.sh <input-folder> [git-url]
```
