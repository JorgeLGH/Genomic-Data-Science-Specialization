#!/usr/bin/python
import sys
import getopt
def usage():
  print ("""
processfasta.py : reads a Fasta file and builds a dictionary with all sequences bigger than a given length

processfasta.py [-h] [-l <length>] <filename>

-h            print this message

-l <length>   filter all sequences with a length smaller than <length> (default <length>=0)

<filename>    the file has to be in FASTA formal
 """)

o, a = getopt.getopt(sys.argv[1:], 'l:h')
opts={}
seqlen=0;

for k,v in o:
  opts[k] = v
if '-h' in opts.keys():
  usage(); sys.exit()
if len(a) < 1:
  usage(); sys.exit("input fasta file is missing")
if '-l' in opts.keys():
  if int(opts['l'])<0 :
    print("Length of sequence should be positive!!"); sys.exit(0)
  seqlen=opts['-l']
