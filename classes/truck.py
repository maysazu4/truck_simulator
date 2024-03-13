class Truck:
    def __init__(self , max_fuel,km_per_liter,wheel_repair_price_per_km,brand):
        self.max_fuel = max_fuel
        self.km_per_liter = km_per_liter
        self.wheel_repair_price_per_km = wheel_repair_price_per_km
        self.brand = brand
        self.curr_fuel = max_fuel
    

    def can_do_it(self, length):
        return length <= (self.curr_fuel*self.km_per_liter)