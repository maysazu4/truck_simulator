from classes.road import Road

def bad(truck,length):
    road = Road(name='bad',terrain_hardness=20,mental_effect="Severe Distress",wheel_damage_effect=3)
    print("The truck has now entered a bad road with a length of {} km".format(length))
    road.calculate_truck_effect(truck,length)
    
     
    
