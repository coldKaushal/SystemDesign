import sys

from ParkingFloor import ParkingFloor
from ParkingSlot import ParkingSlot
from VehicleType import VehicleType
from ParkingLot import ParkingLot
from EntryGate import EntryGate
from ExitGate import ExitGate


if __name__ == "__main__":
    print("Initialising system")
    print("Enter number of floors")
    count_of_floors = int(input())
    list_of_floors = []
    for i in range(count_of_floors):
        print(f"Enter the number of slots of floor {i+1}")
        list_of_slots = []
        count_of_slots = int(input())
        for j in range(count_of_slots):
            try:
                print(f"Enter the type of parking slot for {j + 1}th parking slot. Type supportable are {[Vehicle.value for Vehicle in VehicleType]}")
                parking_type = VehicleType(input())
                slot = ParkingSlot(j + 1, parking_type.value)
                list_of_slots.append(slot)
            except Exception as e:
                raise ValueError(e)
        floor = ParkingFloor(i+1, list_of_slots)
        list_of_floors.append(floor)

    parking_lot = ParkingLot(list_of_floors)
    print("Parking lot initialised")
    print("Enter total entry gates")
    count_of_entry_gates = int(input())
    list_of_entry_gates = []
    for i in range(count_of_entry_gates):
        gate = EntryGate(i+1, parking_lot)
        list_of_entry_gates.append(gate)

    print("Initialising exit gates")
    print("Enter total exit gates")
    count_of_exit_gates = int(input())
    list_of_exit_gates = []
    for i in range(count_of_entry_gates):
        gate = ExitGate(i+1, parking_lot)
        list_of_exit_gates.append(gate)

    print("System Initialised")

    while True:
        print("Enter corresponding serial number to interact")
        print("1. Check availability")
        print("100. Close")
        user_input = int(input())

        if user_input==1:
            print("Enter vehicle type")
            vehicle_type = VehicleType(input())
            is_available = parking_lot.check_availability_for_type(vehicle_type.value)
            if is_available:
                print(f"Parking for type {vehicle_type.value} is available")
            else:
                print(f"Parking for type {vehicle_type.value} is not available")
        if user_input==100:
            sys.exit(0)








