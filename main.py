#!/usr/bin/python3
# written by: atholcomb
# main.py
# Generates a new credit card and
# stores it inside of card_issued.rsa

from issuer import bank_card
from issuer import exp_date
from issuer import cvc_code

def main():
  # retrieve credit card number
  ccnum = bank_card.get_info()
  
  # retreive expiration date
  exp = exp_date.get_info()
  
  # retreive cvc number
  cvc = cvc_code.get_info()
  
  print("Please see card_issued.rsa")
  
  # writes out cc info to card_issued.rsa file
  f = open("card_issued.rsa", "w")
  f.write(f"*******************************************\n")
  f.write(f"John Smith | 123 Main St. Chicago, IL 60007\n")
  f.write(f"cc#: {ccnum} exp: {exp} cvc: {cvc}\n")
  f.write(f"*******************************************\n")
  f.close()

if __name__ == "__main__":
    main()
