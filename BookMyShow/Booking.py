from Show import Show
from BookMyShowEnums import BookingStatus

class Booking:
    def __init__(self, booking_id: str, cinema_id: str, show: Show, status: BookingStatus):
        self.__booking_id = booking_id
        self.__cinema_id = cinema_id
        self.__show = show
        self.__status = status

    def get_booking_id(self):
        return self.__booking_id

    def get_cinema_id(self):
        return self.__cinema_id

    def get_show(self):
        return self.__show

    def get_status(self):
        return self.__status

    def update_status(self, new_status: BookingStatus):
        self.__status = new_status