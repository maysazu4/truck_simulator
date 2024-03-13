from classes.road import Road

def mountainous(truck,length):
    road = Road(name='mountainous',terrain_hardness=30,mental_effect="Moderate stress",wheel_damage_effect=2)
    print("The truck has now entered a mountainous road with a length of {} km".format(length))
    road.calculate_truck_effect(truck,length)