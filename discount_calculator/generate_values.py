#!/usr/bin/python3
# written by: atholcomb
# generate_values.py
# generates a dictionary map of values for the 1000s, 100s and 10s placeholders

from random import randint

# generate_values_1000s instantiates a dict of $1000s
def generate_values_1000s():
  values = {}
  for i in range(5):
    price = randint(1000, 10000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# generate_values_100s instantiates a dict of $100s
def generate_values_100s():
  values = {}
  for i in range(5):
    price = randint(100, 1000)
    discount = randint(1, 99)
    values[price] = discount

  return values

# generate_values_10s instantiates a dict of $10s
def generate_values_10s():
  values = {}
  for i in range(5):
    price = randint(10, 100)
    discount = randint(1, 99)
    values[price] = discount

  return values
