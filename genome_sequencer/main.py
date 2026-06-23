#!/usr/bin/python3
# authored by: atholcomb
# main.py
# implements genome_sequencer()

from time import sleep
from genome_sequencer import genomes

def main():
  for c in range(1, 21):
    sleep(1)
    print(f"DNA-Sequence {str(c).zfill(2)}: {genomes()} -> Verified")

if __name__ == "__main__":
          main()
