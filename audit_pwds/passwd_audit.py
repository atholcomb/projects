#!/usr/bin/python3
# written by: atholcomb
# passwd_audit.py
# Program stores user ids and passwords for a given list of students

import json
from random import choice

def main():
  # 
  stored_pwds = {}
  for n in range(1, 101):   # sets the number of ids and passwords to generate
    stored_pwds["uid"+str(n)] = newPassword(15) # password length

  # stores the user + password into the foo.pwds file
  with open("../foo.pwds", "w") as pw:
    for k, v in stored_pwds.items():
      pw.write(f"user:{k} pass:{v}\n")

# generates a password per complexity below
def newPassword(complexity):
  value = ""
  sp = "@#$%"
  alpha = "abcdefghijklmno"
  numbers = "1234567890"

  for i in range(complexity):
    value += choice(sp+alpha+numbers)

  return value

# invokes the program
if __name__ == "__main__":
        main()
