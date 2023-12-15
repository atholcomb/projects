#!/usr/bin/python3
# written by: atholcomb
# create_tokens.py
# Creates a universally unique identifier as an API token

# import the UUID module
import uuid

def create_tokens(quantity):
  tokens = []

  # range is inclusive with +1
  for idx in range(1, quantity+1):    
    # .uuid4 generates random UUID
    api_token = uuid.uuid4().hex    
    # zfill(2) pads 1s place with a leading zero
    tokens.append(f"Token {str(idx).zfill(2)}: {api_token}")
  
  return '\n'.join(tokens)
