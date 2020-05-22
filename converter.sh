#!/usr/bin/env bash

# Converts a pdf while into a searchable pdf file using ocrmypdf

# chmod +x converter.sh
ocrmypdf --force-ocr $1 $1
