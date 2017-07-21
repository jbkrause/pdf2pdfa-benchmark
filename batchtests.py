#!/usr/bin/env python3

import os
import sys
import shutil
import config

# Fuctions
def veraxml_extrctor(fname):
    output = {'passedRules':None ,'failedRules':None, 'passedChecks':None, 'failedChecks':None}
    xml = open(fname).read()
    for attr in output.keys():
        s1 = attr + '="'
        i1 = xml.find(s1)
        i2 = i1+len(s1)
        i3 = xml.find('"',i2)
        if i1>-1:
            output[attr] = xml[i2:i3]
            
    fR = int(output['failedRules'])
    pR = int(output['passedRules'])
    failedRulesRatio = fR / ( pR + fR)
    
    fC = int(output['failedChecks'])
    pC = int(output['passedChecks'])
    failedChecksRatio = fC / ( fC + pC)
    
    output['failedRulesRatio'] = failedRulesRatio
    output['failedChecksRatio'] = failedChecksRatio
    return output

# Direcories
work_dir = os.getcwd()
scripts_dir = work_dir + os.sep + 'Scripts'
output_dir = work_dir + os.sep + 'Output'
sourcepdfs_dir = work_dir + os.sep + 'SourcePDFs'

# Perpare output directory
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)
os.mkdir(output_dir)

# Copy scripts to output dir
scripts = os.listdir(scripts_dir)
for s in scripts:
    shutil.copy(scripts_dir+os.sep+s, output_dir)

# Copy PDFs to output dir and process them
os.chdir(output_dir)
pdfs = os.listdir(sourcepdfs_dir)
results = []
results_rules = []
results_checks = []
results.append('\t'.join(['','Original']+scripts))
results_rules.append('\t'.join(['','Original']+scripts))
results_checks.append('\t'.join(['','Original']+scripts))

fi = 0
for f in pdfs:
    fi += 1
    print( '\nProcessing file: %s (%s/%s)' % (f,fi,len(pdfs)) )
    print( '===================================================================================' )
    shutil.copy(sourcepdfs_dir+os.sep+f, output_dir)
    line = []
    line_rules = []
    line_checks = []
    line.append(f)
    line_rules.append(f)
    line_checks.append(f)
    # run VeraPdf on original file
    os.system( '%s --format mrr -x %s > %s' % (config.VeraPdfExecutable, f, 'original@' + f + '.VeraPDF.xml') )
    ext = veraxml_extrctor('original@' + f + '.VeraPDF.xml')
    line.append(str(ext))
    line_rules.append(str(ext['failedRulesRatio']))
    line_checks.append(str(ext['failedChecksRatio']))
    
    si = 0
    for s in scripts:
        si += 1
        print( '\n=-> conversion scipt: %s (%s/%s)' % (s,si,len(scripts)) )
        # convert file f to PDFA using script S
        fout = s + '@' + f +'A.pdf'
        os.system( 'bash %s %s %s' % (s,f,fout) )
        # run VeraPDF on converted file
        os.system( '%s --format mrr -x %s > %s' % (config.VeraPdfExecutable, fout, fout+'.VeraPDF.xml') )
        if config.DeleteConvertedFiles:
            os.remove(fout)
        ext = veraxml_extrctor(fout+'.VeraPDF.xml')
        line.append(str(ext))
        line_rules.append(str(ext['failedRulesRatio']))
        line_checks.append(str(ext['failedChecksRatio']))
        
    results.append('\t'.join(line))
    results_rules.append('\t'.join(line_rules))
    results_checks.append('\t'.join(line_checks))

open('REPORT.tsv','w').write('\n'.join(results))
open('REPORT_rules.tsv','w').write('\n'.join(results_rules))
open('REPORT_checks.tsv','w').write('\n'.join(results_checks))
        


