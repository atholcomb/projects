#!/usr/bin/python3
# written by: atholcomb
# solve_acronyms.py
# prints out the acronym for a given string

from acronyms import acronyms_data

def main():
  # cleansed_data stores the (good) non-hyphenated dataset
  cleansed_data = [values.replace('-', ' ').split() for values in acronyms_data().values()]

  for cleansed_str in cleansed_data:
    for idx, string in enumerate(cleansed_str):
      # acronym creates the initial characters from the string
      # using the 0th index and uppercases each 0th character
      # ex: Today I Learned -> TIL
      acronym = cleansed_str[idx][0].upper()
      print(acronym, string)
    print()
      
if __name__ == "__main__":
      print(main())
