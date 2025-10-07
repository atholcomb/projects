#!/usr/bin/python3
# written by: atholcomb
# main.py

from Conversion import Temperature
from random import randrange

""" Print out table row """
print("Celsius\t\tFahrenheit\tKelvin")

def main():
  for i in range(10):
    """
    The for loop creates ten instances of the Temperature object
    -temp- stores a random temporary temp value to pass into the object
    T creates the Temperature object and passes in a random temp range
    The convert() method converts celsius in fahrenheit and kelvin
    """
    temp = randrange(1, 3000) 
    T = Temperature(temp) 
    print(T.convert()) 

if __name__ == "__main__":
        main()
