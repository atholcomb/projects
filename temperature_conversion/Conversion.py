#!/usr/bin/python3
# written by: atholcomb
# Conversion.py
# Program takes a temperature in Celsius and converts
# the given temperature into Fahrenheit and Kelvin

class Temperature:
  def __init__(self, celsius):
    self.celsius = celsius

  def convert(self):
    """ Convert the given Celsius into Fahrenheit and Kelvin """
    fahrenheit = int(self.celsius * (9/5) + 32)
    kelvin = int(self.celsius + 273.1)

    """ 
    u00b0C, u00b0F, u00b0K are the degree symbols 
    for Celsius, Fahrenheit and Kelvin respectively 
    """
    return f"{self.celsius}\u00b0C\t\t{fahrenheit}\u00b0F\t\t{kelvin}\u00b0K"

