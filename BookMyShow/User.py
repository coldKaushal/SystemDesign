from UserBooking import UserBooking
from typing import List

class User:
    def __init__(self, user_name: str, user_id: str, list_of_shows_booked: List[UserBooking], is_authorised: bool):
        self.__user_name = user_name
        self.__user_id = user_id
        self.__list_of_shows_booked = list_of_shows_booked
        self.__is_authorised = is_authorised

    def get_user_name(self):
        return self.__user_name

    def get_user_id(self):
        return self.__user_id

    def get_list_of_shows_booked(self):
        return self.__list_of_shows_booked

    def get_is_authorised(self):
        return self.__is_authorised

    def set_is_authorised(self, is_authorised: bool):
        self.__is_authorised = is_authorised

    def add_new_booking(self, new_show_booking: UserBooking):
        self.__list_of_shows_booked.append(new_show_booking)

    def notify(self, booking: UserBooking):
        print(f"Status for the show {booking.get_show().get_show_name()} updated to {booking.get_status()}")


