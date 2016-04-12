#!/bin/bash
# converts the candidates to pdf files and then puts them in 1 big pdf file in the correct order

source /home/joerivl/LOTAAS-Processing/init.presto20.env.sh

pwd

echo "Sorting on chi-squared "
for file in *.pfd; do printf $file".pdf" >> sort_chi_sqr; grep chi-sqr $file.bestprof | awk '{printf " "$5"\n"}' >> sort_chi_sqr; done
sort -k2 -nr sort_chi_sqr > sort_pdf
I=`grep DM sort_pdf | awk '{printf $1" "}'`
#echo "Generating pdfs"
#ls *.ps | xargs -n 1 ps2pdf
#gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=folded_candidates.pdf $I
