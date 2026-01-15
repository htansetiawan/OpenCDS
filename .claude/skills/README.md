# Custom Claude Code Skills for CDS Processing

This directory contains custom Claude Code skills for processing Common Data Set files.

## 📚 Available Skills

### 1. `/pdf-to-md` - PDF to Markdown Converter
**Convert PDF files to markdown using OCR**

**When Claude will use it:**
- You ask to convert a PDF to markdown
- You mention processing PDF documents
- You want to extract text from PDFs

**Example commands:**
```
User: Convert Harvard.pdf to markdown
User: Process all PDFs in the downloads folder
User: Extract text from the university CDS PDF
```

**What it does:**
- Uses Tesseract OCR to extract text
- Handles multi-page PDFs
- Outputs formatted markdown

---

### 2. `/xls-to-md` - Excel to Markdown Converter
**Convert Excel files (.xls, .xlsx) to markdown**

**When Claude will use it:**
- You ask to convert an Excel file to markdown
- You mention processing .xlsx or .xls files
- You want to extract tables from spreadsheets

**Example commands:**
```
User: Convert UIUC.xlsx to markdown
User: Process the Excel file in downloads/
User: Extract data from the spreadsheet
```

**What it does:**
- Directly reads Excel data (no OCR)
- Preserves table structure
- Fast and accurate

---

### 3. `/cds-pipeline` - Full Automation Pipeline
**End-to-end automation: process files and push to git**

**When Claude will use it:**
- You ask to process multiple files
- You want to automate the entire workflow
- You mention committing or pushing to git

**Example commands:**
```
User: Process all files in raw_files/ and push to git
User: Batch convert the CDS files and commit them
User: Automate processing of the downloads folder
```

**What it does:**
- Processes all PDFs (with OCR)
- Processes all Excel files
- Converts to markdown
- Commits and pushes to git

---

## 🚀 How to Use These Skills

### Automatic (Recommended)

Just ask Claude naturally, and it will automatically use the appropriate skill:

```
You: I have some PDFs in the downloads folder, can you convert them to markdown?

Claude: I'll use the pdf-to-md skill to convert your PDFs to markdown.
[Automatically runs pdf_to_markdown.py on your downloads folder]
```

### Manual (Using slash commands)

You can explicitly invoke a skill:

```
You: /pdf-to-md

Claude: [Loads the PDF to Markdown skill and asks what you want to convert]
```

## 📖 Skill Activation Examples

### Example 1: Converting a Single PDF

```
You: Convert Harvard_CDS_2024.pdf to markdown with high quality

Claude: I'll use the pdf-to-md skill to convert this with high-quality OCR.
[Runs: python tools/pdf_to_markdown.py Harvard_CDS_2024.pdf --dpi 600]

Output: Created Harvard_CDS_2024.md in the documents/ folder
```

### Example 2: Processing Excel Files

```
You: I have UIUC.xlsx that I need in markdown format

Claude: I'll use the xls-to-md skill to convert this Excel file.
[Runs: python tools/xls_to_markdown.py UIUC.xlsx]

Output: Created UIUC.md in the documents/ folder
```

### Example 3: Batch Processing with Git

```
You: Process all the files in raw_files/ and push them to GitHub

Claude: I'll use the cds-pipeline skill to process all files and push to git.
[Runs: python tools/automate_cds_pipeline.py raw_files]

Output:
- Processed 3 Excel files
- Processed 5 PDF files
- Committed changes
- Pushed to remote
```

### Example 4: Just Processing (No Git)

```
You: Convert everything in downloads/ to markdown but don't commit yet

Claude: I'll use the cds-pipeline skill with --skip-git to just process the files.
[Runs: python tools/automate_cds_pipeline.py downloads --skip-git]

Output: All files converted to markdown in documents/
```

## 🎯 When Claude Chooses Which Skill

Claude automatically selects the right skill based on your request:

| Your Request | Claude Uses | Reason |
|--------------|-------------|---------|
| "Convert this PDF..." | `pdf-to-md` | Single PDF mentioned |
| "Process UIUC.xlsx..." | `xls-to-md` | Excel file mentioned |
| "Process this folder and commit..." | `cds-pipeline` | Multiple files + git |
| "Batch convert all PDFs..." | `pdf-to-md` | PDF processing |
| "Extract tables from Excel..." | `xls-to-md` | Excel + tables |
| "Automate the workflow..." | `cds-pipeline` | Automation keyword |

## 🛠️ Skill Configuration

Each skill is configured with:

- **name**: Identifier (used for slash commands)
- **description**: Helps Claude decide when to use it (includes trigger keywords)
- **allowed-tools**: Restricts Claude to specific tools (Bash, Read, Write, etc.)

You can view each skill's full configuration in its `SKILL.md` file:
- `pdf-to-md/SKILL.md`
- `xls-to-md/SKILL.md`
- `cds-pipeline/SKILL.md`

## 📝 Customizing Skills

### Modify a skill:

1. Edit the relevant `SKILL.md` file
2. Update the `description` to change when Claude uses it
3. Modify the commands and examples
4. Save the file - changes take effect immediately

### Add trigger keywords:

Edit the `description` field in `SKILL.md`:

```yaml
---
name: pdf-to-md
description: Convert PDF files to Markdown using OCR. Use when the user wants to convert PDF, extract text, OCR documents, digitize PDFs, or process scanned files.
---
```

Add more keywords that should trigger the skill.

## 🔍 Testing Skills

### Check if skills are loaded:

```
You: What skills are available?

Claude: I have these custom skills available:
- pdf-to-md: Convert PDF files to Markdown
- xls-to-md: Convert Excel files to Markdown
- cds-pipeline: Full automation pipeline with git
```

### Test a specific skill:

```
You: /pdf-to-md
[Claude loads the skill and asks what you want to convert]

You: /xls-to-md
[Claude loads the skill and asks for the Excel file]

You: /cds-pipeline
[Claude loads the skill and asks for input folder]
```

## 📂 Skill File Structure

```
.claude/skills/
│
├── README.md                 # This file
│
├── pdf-to-md/
│   └── SKILL.md             # PDF converter skill definition
│
├── xls-to-md/
│   └── SKILL.md             # Excel converter skill definition
│
└── cds-pipeline/
    └── SKILL.md             # Automation pipeline skill definition
```

The actual Python scripts these skills run are in the `tools/` directory:
- `tools/pdf_to_markdown.py`
- `tools/xls_to_markdown.py`
- `tools/automate_cds_pipeline.py`

## 💡 Pro Tips

1. **Natural language works best**: Just describe what you want, Claude will pick the right skill

2. **Be specific about quality**: Mention "high quality" for PDFs to trigger `--dpi 600`

3. **Mention git explicitly**: If you want git operations, say "commit" or "push"

4. **Review before committing**: Say "but don't commit yet" to use `--skip-git`

5. **Combine with /commit**: Process with `--skip-git`, then use `/commit` for custom messages

## 🔗 Related Documentation

- [CONTRIBUTING.md](../../CONTRIBUTING.md) - Complete processing guide and best practices
- [tools/README.md](../../tools/README.md) - Detailed tool documentation

## ❓ FAQ

**Q: Do I need to install anything for these skills to work?**
A: Yes, install dependencies:
```bash
pip install -r requirements.txt
brew install tesseract poppler  # macOS only
```

**Q: Can I use these skills in any project?**
A: These are project-specific skills. To use globally, copy to `~/.claude/skills/`

**Q: How do I disable a skill?**
A: Rename or delete its SKILL.md file.

**Q: Can I create my own skills?**
A: Yes! See the [Custom Claude Code Skills documentation](https://docs.anthropic.com/claude-code/skills)

**Q: Do these skills work with the /commit skill?**
A: Yes! Process files with `--skip-git`, then use `/commit` for AI-generated commit messages.

---

**Happy processing!** 🎉

These skills make working with Common Data Set files much easier. Just tell Claude what you want in natural language, and it will handle the rest.
