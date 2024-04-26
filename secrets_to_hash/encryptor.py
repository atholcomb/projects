#!/usr/bin/python3
# written by: atholcomb
# encryptor.py
# function encrypts a secret with a hash id

import random

def create_hash():
  hash_id = ""
  hex_code = "abcdef12345678"  # hexidecimal 
  for hash_len in range(9):
    hash_id += random.choice(hex_code)

  return hash_id
