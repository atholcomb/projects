#!/usr/bin/python3
# written by: atholcomb
# solve_acronyms.py
# for a given phrase, solves the acronym (e.g. TIL - Today I Learned)

from strings import phrases

def main():
  # cleansed_data stores the (good) non-hyphenated dataset
  cleansed_data = [values.replace('-', ' ').split() for values in phrases().values()]

  for cleansed_str in cleansed_data:
    for idx, string in enumerate(cleansed_str):
      # acronym creates the initial characters from the string
      # using the 0th index and uppercases each 0th character
      acronym = cleansed_str[idx][0].upper()
      print(acronym, string)
    print()
      
if __name__ == "__main__":
      main()
