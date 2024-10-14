#!/user/bin/python3
# written by: atholcomb
# issuer.py
# Issues a credit card number, CVC code, and Expiration date

def get_cc_number():
  cc_vendor = "Visa"
  name = "Andrew, Holcomb"
  cc_number = "101.332.891.0192"
  exp_date = "10.31.2032"
  cvc_number = "123"
  
  return f"{cc_vendor}\n{name}\ncc_number:{cc_number}\nexpiration:{exp_date}\ncvc_number:{cvc_number}\n"
