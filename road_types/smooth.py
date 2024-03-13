from classes.road import Road

def smooth(truck,length):
    road = Road(name='smooth',terrain_hardness=10,mental_effect="Relaxed",wheel_damage_effect=1)
    print("The truck has now entered a smooth road with a length of {} km".format(length))
    road.calculate_truck_effect(truck,length)