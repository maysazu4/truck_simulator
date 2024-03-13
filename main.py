from truck_simulator import truck_simulator
import sys
import data_load as l


  

def main():
    simulator = truck_simulator()
    truck = l.load_trucks_data('user_input/truck.json')
    roads_list = l.load_roads_data('user_input/roads.json')
    for road in roads_list:
        if simulator.can_do_it(truck, length=road[1]):
            simulator.driveTruckOnRoad(truck,road_type = road[0],length = road[1])
        else:
            print("Not enough fuel to go on the road with type:{} and length:{}".format(road[0],road[1]))
            print('\n')
    

    

if __name__ == "__main__":
    main()