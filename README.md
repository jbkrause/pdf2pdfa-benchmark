# PDFA Conversion Benchmark

Several PDF to PDFA conversion strategies (BASH scripts) are included.

A script is provided to execute all these strategies on each document of an arbitrary collection of PDFs and produce PDFAs. 

PDFA compliance statistics are computed using VerPDF and summary tables are produced (TSV or tab separated values).

## Requirements
 
* BASH, 
* Ghostscript (inckuding the tools ps2pdf and pdf2ps), 
* Python (>=3), 
* ImageMagick,
* [VeraPDF](http://software.verapdf.org/).

## Running the benchmark

1. Copy all PDF files you which to use for the benchmark in the "SourcePDFs" folder. A couple are provided, as an example.
2. Run the command: "python3 batchtests.py"
3. The results are stored in the "Output" folder:
   * Aggregated results: "REPORT_rules.tsv" (fraction of tested rules that failed), "REPORT_checks.tsv" (fraction of tests that failed) and "REPORT.tsv" (detailed report).
   * Detailed VeraPDF report are the files ending by .VersPDF.xml


## About the PDF to PDFA conversion scripts

All the scripts or the "Scripts" folder are executed on each PDF of the collection.

Each script must take exactly tho arguments. The first beeing the input filename, the second the output filename.
