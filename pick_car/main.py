#!/usr/bin/python3
# written by: atholcomb
# main.py
# Program returns the number of car listings per user's choice

from car import list_car

def main():
  number_of_cars = int(input("How many cars would you like to see: "))

  for i in range(number_of_cars):
    list_car()

if __name__ == "__main__":
      main()
