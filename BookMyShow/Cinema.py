from CinemaBooking import CinemaBooking
from BookMyShowEnums import Payment
from User import User
from Show import Show
from typing import List
from UserBooking import UserBooking

class Cinema:
    def __init__(self, cinema_id: str, list_of_bookings: List[CinemaBooking], available_payment_options: List[Payment],
                 list_of_observers: List[List[User], List[UserBooking]]):
        self.__cinema_id = cinema_id
        self.__list_of_bookings = list_of_bookings
        self.__available_payment_options = available_payment_options

    def get_cinema_id(self):
        return self.__cinema_id

    def get_list_of_bookings(self):
        return self.__list_of_bookings

    def get_available_payment_options(self):
        return self.__available_payment_options

    def get_total_bookings(self):
        return len(self.__list_of_bookings)

    def book_show_for_user(self, show: Show, user: User):
        for booking in self.__list_of_bookings:
            if booking.get_show() == show:
                booking.add_new_user(user)

    def add_new_show(self, cinema_booking: CinemaBooking):
        self.__list_of_bookings.append(cinema_booking)

    def remove_show(self, cinema_booking: CinemaBooking):
        check = cinema_booking in self.__list_of_bookings
        if not check:
            print("This show is not present in the list of bookings")
            return
        self.__list_of_bookings.remove(cinema_booking)
