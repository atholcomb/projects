#!/usr/bin/python3
# written by: atholcomb
# solve_acronyms.py
# Finds and solves the acronyms within the acronyms.py module
# Writes out the acronym to the left-hand side of the screen

from acronyms import acronyms_data

def main():
  # cleansed_data stores the (good) non-hyphenated dataset
  cleansed_data = []

  for values in acronyms_data().values():
    # replaces all '-' with a white space character
    # split() creates a indexed based list for each string
    cleansed_data.append(values.replace('-', ' ').split())
    
  for cleansed in cleansed_data:
    for idx, data in enumerate(cleansed):
      # store & uppercase the 'true' acronym inside the variable
      acronym = data[0].upper()
      print(acronym, data)
      # move to next acronym in list once list reaches final index
      if idx == (len(cleansed)-1):
        print()
      
if __name__ == "__main__":
    main()
