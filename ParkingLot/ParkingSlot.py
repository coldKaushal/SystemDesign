
class ParkingSlot:
    def __init__(self, slot_id, parking_type: str):
        self.__slot_id = slot_id
        self.__parking_type = parking_type
        self.__vehicle_id = None
        self.__booked_time = None
        self.__is_occupied = False

    def get_parking_type(self):
        return self.__parking_type

    def get_slot_id(self):
        return self.__slot_id

    def check_availability(self):
        return not self.__is_occupied

    def book_parking_slot(self, vehicle_id, booked_time):
        self.__vehicle_id = vehicle_id
        self.__booked_time = booked_time
        self.__is_occupied = True

    def vacate_parking_slot(self):
        self.__is_occupied = False
        [vehicle_id, booked_time] = [self.__vehicle_id, self.__booked_time]
        self.__vehicle_id, self.__booked_time = None, None
        return [vehicle_id, booked_time]
