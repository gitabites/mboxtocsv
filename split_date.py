#!/usr/bin/env python
import sys
import csv

infile = open(sys.argv[1])
outfile = open(sys.argv[2], 'w')
writer = csv.writer(outfile)

for line in infile:
 splits = line.split(",")
 newline = []
 if len(splits) == 4:
   for i in range(0,3):
     newline.append(splits[i])
 else:
         newline.append("None")
 print newline
 writer.writerow(newline)


infile.close()
outfile.close()	

