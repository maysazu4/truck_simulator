from classes.road import Road

def rough(truck,length):
    road = Road(name='rough',terrain_hardness=45,mental_effect="High Stress",wheel_damage_effect=4)
    print("The truck has now entered a rough road with a length of {} km".format(length))
    road.calculate_truck_effect(truck,length)