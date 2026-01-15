#!/bin/bash
# Simple wrapper script for the CDS automation pipeline
# Usage: ./run_pipeline.sh <input_folder> [output_folder] [git_url]

set -e  # Exit on error

# Default values
INPUT_FOLDER="${1:-.}"
OUTPUT_FOLDER="${2:-output}"
GIT_URL="${3:-}"
DPI="${DPI:-300}"

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}======================================${NC}"
echo -e "${GREEN}CDS Automation Pipeline${NC}"
echo -e "${GREEN}======================================${NC}"
echo ""

# Check if input folder exists
if [ ! -d "$INPUT_FOLDER" ]; then
    echo -e "${RED}Error: Input folder not found: $INPUT_FOLDER${NC}"
    exit 1
fi

# Build command
CMD="python automate_cds_pipeline.py \"$INPUT_FOLDER\" -o \"$OUTPUT_FOLDER\""

if [ -n "$GIT_URL" ]; then
    CMD="$CMD --git-url \"$GIT_URL\""
fi

if [ -n "$DPI" ] && [ "$DPI" != "300" ]; then
    CMD="$CMD --dpi $DPI"
fi

# Show what we're running
echo -e "${YELLOW}Running:${NC} $CMD"
echo ""

# Execute
eval $CMD

exit $?
