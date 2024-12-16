from VehicleMultiplier import VehicleMultiplier
import datetime
from SlotType import SlotType
class Bill:
    def __init__(self, vehicle_id: str, vehicle_type: SlotType, floor_number: int, slot_id: str, booking_time: datetime.datetime, exit_time: datetime.datetime):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__floor_number = floor_number
        self.__slot_id = slot_id
        self.__booking_time = booking_time
        self.__exit_time = exit_time

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def get_floor_number(self):
        return self.__floor_number

    def get_slot_id(self):
        return self.__slot_id

    def get_booking_time(self):
        return self.__booking_time

    def get_exit_time(self):
        return self.__exit_time

    def get_total_amount(self):
        total_time = self.__exit_time - self.__booking_time
        multiplier = VehicleMultiplier.get_multiplier(self.__vehicle_type)
        return multiplier * total_time