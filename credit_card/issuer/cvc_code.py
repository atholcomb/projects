#!/usr/bin/python3
# written by: atholcomb
# get_info.py
# returns the cvc number for a credit card

from random import randint

def get_info():
  cvc = ''

  for i in range(3):
    cvc += str(randint(0,9)) 

  return f"{cvc}"
