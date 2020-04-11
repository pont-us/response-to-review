#!/bin/bash

set -e

rm -f *.aux *.bbl *.blg *.lof *.log *.out *.toc

# Convert "minor comments" table(s) to LaTeX.

./makeresp.py --input table-1.txt --output table-1.tex
# ./makeresp.py --input table-2.txt --output table-2.tex
# ./makeresp.py --input table-3.txt --output table-3.tex

# Process LaTeX file to extract citations.

pdflatex -draftmode responses.tex

# Extract only the needed BibTeX records from a master bibliography and
# write them to a specialized bibliography for this document only.
# Normally, the master bibliography would live outside this repository.

bibtool -i master.bib \
        -x responses.aux \
        -- 'delete.field { keywords }' \
        -- 'delete.field { abstract }' \
        -- 'delete.field { mynote }' \
	-- 'rename.field { url=urlxxx if doi="/" }' \
	-- 'delete.field { urlxxx }' \
        > refs.bib

bibtex responses
pdflatex responses
pdflatex responses
