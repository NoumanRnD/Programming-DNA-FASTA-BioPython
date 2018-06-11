import os
from pyfaidx import Fasta
 
 
 
 

def fasta_reader(filename):
  from Bio.SeqIO.FastaIO import FastaIterator
  with open(filename) as handle:
    for record in FastaIterator(handle):
      yield record 

def Main():
   seq = 0
   
   lenAllseq = []
   lenallseqc = 0
   header = []
   file = raw_input("Enter the file name :  ")
   print("Report for file " + file)
   for entry in fasta_reader(file):       
       seq =seq +1       
       lenallseqc = lenallseqc + len(entry.seq)
       lenAllseq.append(entry.seq)

   maxi = len(str(max(lenAllseq, key=len)))
   mini = len(str(min(lenAllseq, key=len)))
   print("Number of sequences :" + str(seq))
   print("Total sequence length :" + str(lenallseqc))
   print("Maximum sequence length :" +str(maxi) )
   print("Minimum sequence length :" + str(mini))
   total_avg = sum( map(len, lenAllseq) ) / len(lenAllseq)
   print("Average sequence length :" + str(total_avg))

   i= 0
   for entry in fasta_reader(file):
       i = i + 1
       print str(">" + entry.id +" "+ str(i))
       print  ("length : " + str(len(entry.seq)))
       print ("A: "+ str(entry.seq.lower().count('a')))
       print ("C: "+ str(entry.seq.lower().count('c')))
       print ("G: "+ str(entry.seq.lower().count('g')))
       print ("T: "+ str(entry.seq.lower().count('t')))
Main()	

 
