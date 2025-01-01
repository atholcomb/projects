#!/usr/bin/python3
# written by: atholcomb
# car.py
# Implements the pick_car() function to return a list of cars

from vehicle import vehicle
import random as r
import json

def list_car():
  year = ""
  make = ""
  model =  ""
  trim = ""

  car = {
          "year":"2026",
          "make":["BMW"],
          "make":["Subaru","Toyota", "BMW", "Audi"],
          "models":[
                    ["Legacy","Forester","Impreza","Outback"],
                    ["Corolla","Camry","Rav-4","Venza"],
                    ["3Series","5Series","7Series","MSeries"],
                    ["S4","Q3","Q4","Q7"],
                   ],
          "trim":[
                  ["Base", "Platinum","Limited","Touring"],
                  ["LE", "SE","XLE","XSE"],
                  ["30i", "50i","70i","xDrive"],
                  ["Base", "Premium","Premium-Plus","Prestige"],
                 ],
        }

  choice = r.choice(car["make"])
  if "Subaru" in choice:
    make = choice
    year = r.randrange(1980, 2025)
    model = r.choice(car["models"][0])
    trim = r.choice(car["trim"][0])
  elif "Toyota" in choice:
    make = choice
    year = r.randrange(1980, 2025)
    model = r.choice(car["models"][1])
    trim = r.choice(car["trim"][1])
  elif "BMW" in choice:
    make = choice
    year = r.randrange(1980, 2025)
    model = r.choice(car["models"][2])
    if "3Series" in model:
      trim = car["trim"][2][0]
    elif "5Series" in model:
      trim = car["trim"][2][1]
    elif "7Series" in model:
      trim = car["trim"][2][2]
    elif "MSeries" in model:
      trim = car["trim"][2][3]
  elif "Audi" in choice:
    make = choice
    year = r.randrange(1980, 2025)
    model = r.choice(car["models"][3])
    trim = r.choice(car["trim"][3])

  # vehicle.get_vehicle_info() method returns one car object
  # and creates a json blob from the object
  v = vehicle(year,make,model,trim)
  print(json.dumps(v.get_vehicle_info(), indent=2))
