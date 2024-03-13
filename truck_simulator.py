import utils

class truck_simulator:
    def __init__(self):
        self.road_types = utils.load_road_types()
    
    def driveTruckOnRoad(self,truck,road_type,length):
        if road_type in self.road_types:
            return self.road_types[road_type](truck,length)
        else:
            print("Road type not found")
            return False
        
    def can_do_it(self,truck,length):
        return truck.can_do_it(length)
    
