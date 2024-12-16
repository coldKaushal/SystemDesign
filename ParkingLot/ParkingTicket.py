

class ParkingTicket:
    def __init__(self, vehicle_id, vehicle_type, floor_number, slot_id, booking_time):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__floor_number = floor_number
        self.__slot_id = slot_id
        self.__booking_time = booking_time

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


