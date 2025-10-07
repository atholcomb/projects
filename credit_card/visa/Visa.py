#!/usr/bin/python3
# written by: atholcomb
# Visa.py
# program generates a credit card number, cvc code, and exp date

from random import randint, randrange

class Merchant:
    def __init__(self, owner="John Doe"):
      self.owner = owner 
   
    """ generates credit card number """
    def cc_number(self):
      cc_value_1 = ''
      cc_value_2 = ''
      cc_value_3 = ''
      cc_value_4 = ''

      for i in range(4):
        # 43 standardizes the Visa Credit Card format
        cc_value_1 = str(43) + str(randint(0,9)) + str(randint(0,9))
        # The remaining values make up the credit card with arbitary numbers
        cc_value_2 += str(randint(0,9))
        cc_value_3 += str(randint(0,9))
        cc_value_4 += str(randint(0,9))

      return f"{cc_value_1}-{cc_value_2}-{cc_value_3}-{cc_value_4}"

    """ generates expiration date """
    def exp_date(self):
      month = ''
      year = ''

      month = str(randint(1, 12))
      year = str(randint(25, 30))

      return f"{month}/{year}"

    """ generates cvc number """
    def cvc_code(self):
      cvc = ''

      for i in range(3):
        cvc += str(randint(0,9)) 

      return f"{cvc}"
