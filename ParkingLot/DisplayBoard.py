from ParkingFloor import ParkingFloor
from VehicleType import VehicleType


class DisplayBoard:
    def __init__(self, display_board_id, parking_floor: ParkingFloor):
        self.display_board_id = display_board_id
        self.parking_floor = parking_floor

    def show_availability_for_each_type(self):
        availability_chart = {}
        for Vehicle in VehicleType:
            availability_chart[Vehicle.value] = self.parking_floor.check_available_slots_for_type(Vehicle.value)
        return availability_chart




