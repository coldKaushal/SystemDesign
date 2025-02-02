from enum import Enum


class Genre(Enum):
    SciFi = "sci-fi"
    ROMANCE = "romance"
    COMEDY = "comedy"
    ACTION = "action"


class BookingStatus(Enum):
    BOOKED = "booked"
    CANCELLED = "cancelled"
    AVAILABLE = "available"


class Payment(Enum):
    CARD = "card"
    CASH = "cash"
    UPI = "upi"
