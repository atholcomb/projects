#!/usr/bin/python3
# written by: atholcomb
# get_info.py
# returns a credit card number

from random import randint

def get_info():
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
