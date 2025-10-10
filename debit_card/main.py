#!/usr/bin/python3
# written by: atholcomb
# main.py

from Merchant import Merchant

def main():
    c = Merchant("Paul Holcomb")
  
    # write out the card details to card_issued.rsa
    with open("card_issued.rsa", "w") as f:
      f.write("Visa Debit Card\n")
      f.write(f'{c.owner}\n{c.cc_number()}\nexp:{c.exp_date()} cvc:{c.cvc_code()}')
    
    # open card_issued.rsa and show debit card information
    with open("card_issued.rsa", "r") as f:
      data = f.read()
      print(data)


if __name__ == "__main__":
        main()
