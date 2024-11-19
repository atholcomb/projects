#!/usr/bin/python3
# written by: atholcomb
# main.py
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.

from generate_values import generate_values_1000s
from generate_values import generate_values_100s
from generate_values import generate_values_10s
from find_discounts import find_discount_1s_place
from find_discounts import find_discount_2s_place
from find_discounts import find_discount_10s_place

def main():
  print("1,000's Discount Dollar Amount ($Amt)")
  print("Discount = Per%   $Amt  $Difference")

  for price, discount in generate_values_1000s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))
   
  print("\n100's Discount Dollar Amount ($Amt)")
  print("Discount = Per%   $Amt  $Difference")

  for price, discount in generate_values_100s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_2s_place(price, discount))

  print("\n10's Discount Dollar Amount ($Amt)")
  print("Discount = Per%   $Amt $Difference")

  for price, discount in generate_values_10s().items():
    if discount % 10 == discount:
      print(find_discount_1s_place(price, discount))
    elif discount % 100 == discount:
      print(find_discount_10s_place(price, discount))
 
if __name__ == "__main__":
        main()
