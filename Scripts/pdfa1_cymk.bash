#!/bin/bash

gs -dPDFA=1 -dBATCH -dNOPAUSE -sProcessColorModel=DeviceCMYK -sDEVICE=pdfwrite -sOutputFile=$2 $1

