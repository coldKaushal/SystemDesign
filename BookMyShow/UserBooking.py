from Booking import Booking
from BookMyShowEnums import BookingStatus, Payment
from Show import Show


class UserBooking(Booking):
    def __init__(self, booking_id: str, cinema_id: str, show: Show, status: BookingStatus, payment_mode: Payment):
        super().__init__(booking_id, cinema_id, show, status)
        self.__payment_mode = payment_mode

    def update_status(self, new_status: BookingStatus):
        super().update_status(new_status)

    def get_payment_mode(self):
        return self.__payment_mode

