#!/usr/bin/python3
# written by: atholcomb
# find_discounts.py
# Program outputs and formats the values of the discounts applied

# find_discount_1s_place calls the 1s place output formatter
def find_discount_1s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  return f"${answer:<7} = .{discount}% of ${price} (${price:>2} - ${((price * discount) / 100)})"

# find_discount_2s_place calls the 2s place output formatter
def find_discount_2s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  return f"${answer:<7} = {discount}% of ${price} (${price:>2} - ${((price * discount) / 100)})"

# find_discount_10s_place calls the 10s place output formatter
def find_discount_10s_place(price, discount):
  answer = round(price - ((price * discount) / 100), 2)
  return f"${answer:<7} = {discount}% of ${price} (${price} - ${((price * discount) / 100)})"
 
