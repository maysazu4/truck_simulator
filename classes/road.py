class Road:
    def __init__(self,name,terrain_hardness,mental_effect,wheel_damage_effect):
        self.name = name
        self.terrain_hardness = terrain_hardness
        self.mental_effect = mental_effect
        self.wheel_damage_effect = wheel_damage_effect

    def calculate_truck_effect(self,truck,length):
        fuel_effect = round(truck.curr_fuel - (length/truck.km_per_liter),2)
        
        print('The fuel in the truck has decreased from {} to {} '.format(truck.curr_fuel, fuel_effect))
        truck.curr_fuel = fuel_effect
        wheel_damage = round( length *self.wheel_damage_effect/truck.wheel_repair_price_per_km)
        print('The cost to fix the wheel damage is ${}.'.format(wheel_damage))

        print('Your mental health status is: {}'.format(self.mental_effect))
        print('\n') 
        

        

