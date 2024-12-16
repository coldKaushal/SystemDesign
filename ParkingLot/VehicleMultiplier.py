
class VehicleMultiplier:
    CAR = 20
    TRUCK = 50
    BIKE = 10
    BUS = 30

    def get_multiplier(self, vehicle_type: str):
        if vehicle_type == "CAR":
            return self.CAR
        elif vehicle_type == "TRUCK":
            return self.TRUCK
        elif vehicle_type == "BIKE":
            return self.BIKE
        elif vehicle_type == "BUS":
            return self.BUS