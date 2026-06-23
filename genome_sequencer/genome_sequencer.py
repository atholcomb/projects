#!/usr/bin/python3
# authored by: atholcomb
# genome_sequencer.py
# returns a sequence of {n} dna strands

from random import choice

def genomes():
  sequence = ""
  dna_strand = "atgc"
  
  for strand_count in range(15):
    sequence += choice(dna_strand)
    
  return sequence
