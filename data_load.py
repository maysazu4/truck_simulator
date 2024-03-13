import json
from classes.truck import Truck

def load_roads_data(file):
    with open(file) as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    l = []
    for object in parsed_json:
        a = (object['road_type'] , object['length'])
        l.append(a)
    return l 

def load_trucks_data(file):
    with open(file) as user_file:
        file_contents = user_file.read()
    parsed_json = json.loads(file_contents)
    for object in parsed_json:
        a = Truck(object['max_fuel_amount'] , object['km_per_liter'],
             object['price_repair_wheels_per_km'],object['brand'])  
    return a 
