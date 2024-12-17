from SlotType import SlotType

class VehicleMultiplier:
    def get_multiplier(self, vehicle_type: SlotType):
        if vehicle_type == SlotType.CAR:
            return 20
        elif vehicle_type == SlotType.BIKE:
            return 10
        elif vehicle_type == SlotType.TRUCK:
            return 50
        elif vehicle_type == SlotType.BUS:
            return 40
