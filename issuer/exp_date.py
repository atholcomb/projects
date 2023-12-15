#!/usr/bin/python3
# written by: atholcomb
# get_info.py
# returns the expiration date for a credit card

from random import randint

def get_info():
  month = date = ''

  month = str(randint(1, 12))
  date = str(randint(1, 30))

  return f"{month}/{date}"
