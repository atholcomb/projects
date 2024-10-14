#!/usr/bin/python3
# written by: atholcomb
# main.py
# calls the issuer.py program to instantiate a new credit card

from issuer import get_cc_number

def main():
  f = open("visa_cc.rsa", "w")
  f.write(get_cc_number())
  f.close()

if __name__ == "__main__":
        main()
