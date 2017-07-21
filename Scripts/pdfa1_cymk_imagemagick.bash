#!/bin/bash

convert -density 150 -trim -quality 80 $1 $1.imagemagick.pdf

gs -dPDFA=1 -dBATCH -dNOPAUSE -sProcessColorModel=DeviceCMYK -sDEVICE=pdfwrite -sOutputFile=$2 $1.imagemagick.pdf

rm $1.imagemagick.pdf

