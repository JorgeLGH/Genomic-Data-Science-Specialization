#!/usr/bin/python
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""
import getopt
import sys
filename=sys.argv[1]
o, a = getopt.getopt(sys.argv[1:], 'l:h')
print(len(a))


try:
  f = open(filename)
except IOError:
  print("The file %s does not exist!" % filename)
