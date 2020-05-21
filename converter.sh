#!/bin/bash

# Converts a pdf while into a searchable pdf file using ocrmypdf

ocrmypdf --force-ocr $1 $1
