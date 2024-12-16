import sys

from ParkingLot import ParkingLot
from ParkingTicket import ParkingTicket


class EntryGate:
    def __init__(self, gate_id, parking_lot:ParkingLot):
        self.__gate_id = gate_id
        self.__parking_lot = parking_lot

    def get_gate_id(self):
        return self.__gate_id

    def check_availability(self, vehicle_type):
        return self.__parking_lot.check_availability_for_type(vehicle_type)

    def book_parking_slot(self, vehicle_type, vehicle_id, booked_time):
        try:
            [floor_number, slot_id] = self.__parking_lot.get_available_parking(vehicle_type)
            self.__parking_lot.book_parking_slot(vehicle_id, floor_number, slot_id, booked_time)
            parking_ticket = ParkingTicket(vehicle_id, vehicle_type, floor_number, slot_id, booked_time)
            return parking_ticket

        except Exception as e:
            print(e)
            sys.exit(1)







