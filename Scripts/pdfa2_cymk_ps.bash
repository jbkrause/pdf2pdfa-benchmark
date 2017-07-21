#!/bin/bash

pdf2ps $1 $1.ps          # pdf is converted to postscript
ps2pdf $1.ps $1.ps.pdf   # postscript is converted back to pdf
rm $1.ps                 # cleanup
gs -dPDFA=2 -dBATCH -dNOPAUSE -sProcessColorModel=DeviceCMYK -sDEVICE=pdfwrite -sOutputFile=$2 $1.ps.pdf
rm $1.ps.pdf             # cleanup
