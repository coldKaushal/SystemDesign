from ParkingFloor import ParkingFloor
from typing import List


class ParkingLot:
    def __init__(self, list_of_parking_floors: List[ParkingFloor]):
        self.__list_of_parking_floors = list_of_parking_floors

    def check_availability_for_type(self, vehicle_type):
        for floor in self.__list_of_parking_floors:
            if floor.check_available_slots_for_type(vehicle_type):
                return True

        return False

    def get_available_parking(self, vehicle_type):
        for floor in self.__list_of_parking_floors:
            if self.check_availability_for_type(vehicle_type):
                return floor.get_parking_slot_details(vehicle_type)

        raise ValueError("No available slots right now")

    def book_parking_slot(self, vehicle_id, floor_number, slot_id, booking_time):
        for floor in self.__list_of_parking_floors:
            if floor.get_parking_floor() == floor_number:
                return floor.book_parking_slot(slot_id, vehicle_id, booking_time)
        raise ValueError("Invalid floor number")

    def vacate_parking_slot(self, floor_number, slot_id):
        for floor in self.__list_of_parking_floors:
            if floor.get_parking_floor()==floor_number:
                return floor.vacate_parking_slot(slot_id)
        raise ValueError("Invalid Floor Number")



