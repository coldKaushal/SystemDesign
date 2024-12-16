import datetime

from ParkingFloor import ParkingFloor
from SlotType import SlotType
from typing import List
from SlotType import SlotType
from ParkingTicket import ParkingTicket


class ParkingLot:
    def __init__(self, parking_lot_id: str, list_of_floors: List[ParkingFloor]):
        self.__parking_lot_id = parking_lot_id
        self.__list_of_floors = list_of_floors

    def get_parking_lot_id(self):
        return self.__parking_lot_id

    def get_list_of_floors(self):
        return self.__list_of_floors

    def check_available_slot_for_type(self, slot_type:SlotType):
        for floor in self.__list_of_floors:
            available_slot = floor.get_check_availability_for_type(slot_type)
            if available_slot >0:
                return True

        return False

    def get_available_slot_detail_for_type(self, slot_type: SlotType):
        for floor in self.__list_of_floors:
            available_slot = floor.get_check_availability_for_type(slot_type)
            if available_slot > 0:
                slot_id = floor.get_available_slot_id(slot_type)
                return [floor.get_floor_number(), slot_id]

        raise ValueError("No slot available for the slot type")

    def book_slot(self, floor_number: int, slot_id: str, vehicle_id:str, slot_type: SlotType, booking_time: datetime.datetime):
        for floor in self.__list_of_floors:
            if floor.get_floor_number()==floor_number:
                if floor.get_check_availability_for_type(slot_type):
                    return floor.book_slot(vehicle_id, slot_id, booking_time)
                else:
                    raise ValueError("No slot available")

        raise ValueError("Invalid floor number")

    def vacate_slot(self, parking_ticket: ParkingTicket):
        floor_number = parking_ticket.get_floor_number()

        for floor in self.__list_of_floors:
            if floor.get_floor_number()==floor_number:
                return floor.vacate_slot(parking_ticket)

        raise ValueError("Invalid floor number retrieved from parking_ticket")
