import sys

from ParkingLot import ParkingLot
from Bill import Bill


class ExitGate:
    def __init__(self, gate_number, parking_lot: ParkingLot):
        self.__gate_number = gate_number
        self.__parking_lot = parking_lot

    def vacate_parking_slot(self, floor_number, slot_id, vehicle_type, exit_time):
        try:
            [vehicle_id, booking_time] = self.__parking_lot.vacate_parking_slot(floor_number, slot_id)
            bill = Bill(vehicle_id, vehicle_type, floor_number, slot_id, booking_time, exit_time)
            return bill

        except Exception as e:
            print(e)
            sys.exit(1)
