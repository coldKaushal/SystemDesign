from Booking import Booking
from BookMyShowEnums import BookingStatus
from Show import Show
from User import User
from typing import List


class CinemaBooking(Booking):
    def __init__(self, booking_id: str, cinema_id: str, show: Show, status: BookingStatus, list_of_users: List[User]):
        super().__init__(booking_id, cinema_id, show, status)
        self.__list_of_users = list_of_users

    def add_new_user(self, new_user):
        self.__list_of_users.append(new_user)

    def update_status(self, new_status: BookingStatus):
        super().update_status(new_status)

