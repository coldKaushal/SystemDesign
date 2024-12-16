from multiprocessing.managers import Value

from ParkingSlot import ParkingSlot
from typing import List


class ParkingFloor:
    def __init__(self, parking_floor, list_of_parking_slots: List[ParkingSlot]):
        self.__parking_floor = parking_floor
        self.__list_of_parking_slots = list_of_parking_slots

    def get_parking_floor(self):
        return self.__parking_floor

    def check_available_slots_for_type(self, vehicle_type: str):
        count = 0
        for slot in self.__list_of_parking_slots:
            if slot.get_parking_type() == vehicle_type and slot.check_availability():
                count += 1
        return count

    def get_parking_slot_details(self, vehicle_type: str):
        if not self.check_available_slots_for_type(vehicle_type):
            raise ValueError("No available slots right now")

        for slot in self.__list_of_parking_slots:
            if slot.get_parking_type() == vehicle_type and slot.check_availability():
                return [self.__parking_floor, slot.get_slot_id()]

        raise ValueError("No available slots right now")

    def book_parking_slot(self, slot_id, vehicle_id, booking_time):
        for parking_slots in self.__list_of_parking_slots:
            if parking_slots.get_slot_id()==slot_id:
                parking_slots.book_parking_slot(vehicle_id, booking_time)
        raise ValueError("Invalid slot id")

    def vacate_parking_slot(self, slot_id):
        for parking_slot in self.__list_of_parking_slots:
            if parking_slot.get_slot_id()==slot_id:
                return parking_slot.vacate_parking_slot()
        raise ValueError("Invalid slot id")
