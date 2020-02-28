#!/bin/bash

set -e

./makeresp.py --input table-in.txt --output table.tex
pdflatex responses.tex
pdflatex responses.tex
