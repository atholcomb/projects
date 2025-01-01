#!/usr/bin/python3
# written by: atholcomb
# vehicle.py
# Module creates vehicle object with four values;
# Year, Make, Model and Trim

class vehicle():
  def __init__(self, year, make, model, trim):
    self.year = year
    self.make = make
    self.model = model
    self.trim = trim

  def get_vehicle_info(self):
    return self.year, self.make, self.model, self.trim
