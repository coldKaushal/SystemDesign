import datetime

from SlotType import SlotType
from ParkingTicket import ParkingTicket
from Bill import Bill

class ParkingSlot:
    def __init__(self, slot_id: str, slot_type: SlotType):
        self.__slot_id = slot_id
        self.__slot_type = slot_type
        self.__is_available = True
        self.__booking_time = None
        self.__vehicle_id = None

    def get_slot_id(self):
        return self.__slot_id

    def get_slot_type(self):
        return self.__slot_type

    def check_availability(self):
        return self.__is_available

    def book_slot(self, vehicle_id: str, booking_time: datetime.datetime, floor_number: int):
        self.__is_available = False
        self.__vehicle_id = vehicle_id
        self.__booking_time = booking_time
        parking_ticket = ParkingTicket(vehicle_id, self.__slot_type, floor_number, self.__slot_id, booking_time)
        return parking_ticket

    def vacate_slot(self, parking_ticket: ParkingTicket):
        self.__is_available = True
        self.__booking_time = None
        self.__vehicle_id = None
        vehicle_id = parking_ticket.get_vehicle_id()
        vehicle_type = parking_ticket.get_vehicle_type()
        booking_time = parking_ticket.get_booking_time()
        floor_number = parking_ticket.get_floor_number()
        time = datetime.datetime.now()
        bill = Bill(vehicle_id, vehicle_type, floor_number, self.__slot_id, booking_time, time)
        return bill

