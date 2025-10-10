#!/usr/bin/python3
# written by: atholcomb
# Merchant.py
# program generates a debit card with a cvc code and exp date

from random import randint

class Merchant:
    def __init__(self, owner="Andrew Holcomb"):
      self.owner = owner 
   
    """ generates credit card number """
    def cc_number(self):
      cc_value_1 = ''
      cc_value_2 = ''
      cc_value_3 = ''
      cc_value_4 = ''

      for i in range(4):
        # 43 standardizes on the Visa credit card format
        cc_value_1 = str(43) + str(randint(0,9)) + str(randint(0,9))
        # The remaining values make up the credit card with real numbers
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
