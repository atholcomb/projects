#!/usr/bin/python3
# written by: atholcomb
# Merchant.py

from Visa import Merchant

def main():
    name = input("Enter the name for the card to be isssued: ") 

    # create credit card object
    card = Merchant(name)
  
    # write out the card details to card_issued.rsa
    with open("card_issued.rsa", "w") as f:
      f.write("Visa Debit Card\n")
      f.write(f'{card.owner}\n{card.cc_number()}\nEXP:{card.exp_date()} CVC:{card.cvc_code()}')
    
    # read the card details and output back to user
    with open("card_issued.rsa", "r") as f:
      data = f.read()
      print(data)

if __name__ == "__main__":
         main()
