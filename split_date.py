#!/usr/bin/env python
import sys
import csv

infile = open(sys.argv[1])
outfile = open(sys.argv[2], 'w')
writer = csv.writer(outfile)

for line in infile:	
  splits = line.split(",")
  newline = []
  newline.append(splits[0])
  print newline
  newline.append(splits[1])
  print newline
  newline.append(splits[2])
  print newline
  if len(splits)> 3:
  	newline.append(splits[3])	
  else:
  	newline.append("None")	
  writer.writerow(newline)

infile.close()
outfile.close()	

