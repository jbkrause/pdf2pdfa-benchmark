#!/bin/bash

gs -dPDFA=2 -dBATCH -dNOPAUSE -sProcessColorModel=DeviceCMYK -sDEVICE=pdfwrite -sOutputFile=$2 $1

