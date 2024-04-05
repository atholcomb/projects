#!/usr/bin/python3
# written by: atholcomb
# main.py
# Generates a new credit card and
# stores it inside of card_issued.rsa

from issuer import get_cc_number
from issuer import get_cvc_code
from issuer import get_exp_date

def main():
  # retrieve credit card number
  ccnum = get_cc_number()
  
  # retreive expiration date
  exp = get_exp_date()
  
  # retreive cvc number
  cvc = get_cvc_code()
  
  print("Please `cat` card_issued.rsa")
  
  # writes out cc info to card_issued.rsa file
  f = open("card_issued.rsa", "w")
  f.write(f"*******************************************\n")
  f.write(f"John Smith | 123 Main St. Chicago, IL 60007\n")
  f.write(f"cc#:{ccnum} exp:{exp} cvc:{cvc}\n")
  f.write(f"*******************************************\n")
  f.close()

if __name__ == "__main__":
    main()
