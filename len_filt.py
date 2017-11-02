#!/usr/bin/env python2

from Bio import SeqIO
import argparse
import re

parser=argparse.ArgumentParser(description='Script for splitting a fatsa file for long and short sequences')
parser.add_argument('--fna', dest='path', required=True, nargs='?', help='Multifasta file with DNA sequences (required)')
parser.add_argument('--lenlim', dest='treshold', default=1000, nargs='?', help='Filter out sequences shorter than the limit. Default = 1000')
args = parser.parse_args()


short_sequences = [] # Setup an empty list
long_sequences = [] # Setup an empty list
for record in SeqIO.parse(open(args.path, "rU"), "fasta") :
  if len(record.seq) < int(args.treshold) :			
    short_sequences.append(record) # Add this record to our list
  if len(record.seq) >= int(args.treshold) :			
    long_sequences.append(record) # Add this record to our list	
#output 
outputn1=args.path+"_bigger"+str(args.treshold)+".fasta"
outputn2=args.path+"_smaller"+str(args.treshold)+".fasta"
output_handle = open(outputn1, "w")
SeqIO.write(long_sequences, output_handle, "fasta")
output_handle.close()
output_handle = open(outputn2, "w")
SeqIO.write(short_sequences, output_handle, "fasta")
output_handle.close()
print "%i Sequences smaller than threshold" % len(short_sequences)
print "%i Sequences bigger than threshold" % len(long_sequences)