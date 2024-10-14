#!/usr/bin/python3
# written by: atholcomb
# issuer.py
# program returns credit card number, cvc code, and exp date

from random import randint

##############################
# generates credit card number
##############################
def get_cc_number():
  set_1 = ''
  set_2 = ''
  set_3 = ''
  set_4 = ''

  for i in range(4):
    set_1 += str(randint(5,7))
    set_2 += str(randint(0,9))
    set_3 += str(randint(0,9))
    set_4 += str(randint(0,9))


  return f"{set_1}-{set_2}-{set_3}-{set_4}"

#######################
# generates cvc number
######################
def get_cvc_code():
  cvc = ''

  for i in range(3):
    cvc += str(randint(0,9)) 

  return f"{cvc}"

###########################
# generates expiration date
###########################
def get_exp_date():
  month = date = ''

  month = str(randint(1, 12))
  date = str(randint(1, 30))

  return f"{month}/{date}"
