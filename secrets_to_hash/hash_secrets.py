#!/usr/bin/python3
# written by: atholcomb
# hash_secrets.py
# creates an hexidecimal cipher  
# from secrets.txt file

import json
from encryptor import create_hash

def main():
  # stores key/value mapping of secret/hash
  hash_dict = {}

  # opens the 'secret.txt' file
  with open('secrets.txt', 'r') as f:
    secrets = json.load(f)

  # creates a hash for each secret
  for key, value in secrets.items():
    hash_dict[value] = create_hash()

  # prints secrets in JSON format
  print(json.dumps(hash_dict, indent=4))


if __name__ == "__main__":
    main()
