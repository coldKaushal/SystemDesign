from ParkingSlot import ParkingSlot
from SlotType import SlotType
from typing import List
from ParkingTicket import ParkingTicket
from Bill import Bill


class ParkingFloor:
    def __init__(self, floor_number, list_of_parking_slots: List[ParkingSlot]):
        self.__floor_number = floor_number
        self.__list_of_parking_slots = list_of_parking_slots

    def get_floor_number(self):
        return self.__floor_number

    def get_list_of_parking_slots(self):
        return self.__list_of_parking_slots

    def get_check_availability_for_type(self, slot_type: SlotType):
        count = 0
        for slot in self.__list_of_parking_slots:
            if slot.get_slot_type() == slot_type and slot.check_availability():
                count += 1
        return count

    def get_available_slot_id(self, slot_type: SlotType):
        for slot in self.__list_of_parking_slots:
            if slot.get_slot_type()==slot_type and slot.check_availability():
                return slot.get_slot_id()

        raise ValueError("No slot available for this type")

    def book_slot(self, vehicle_id, slot_id, booking_time) -> ParkingTicket:
        for slot in self.__list_of_parking_slots:
            if slot.get_slot_id()==slot_id:
                if not slot.check_availability():
                    raise ValueError("Slot is already booked")
                return slot.book_slot(vehicle_id, booking_time)

        raise ValueError("Invalid slot id")

    def vacate_slot(self, parking_ticket: ParkingTicket) -> Bill:
        slot_id = parking_ticket.get_slot_id()
        for slot in self.__list_of_parking_slots:
            if slot.get_slot_id()==slot_id:
                return slot.vacate_slot(parking_ticket)

        raise ValueError("Invalid slot id")



