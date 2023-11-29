from ParkingLot import ParkingLot

from math import floor, log10


class Car:

    def __init__(self, license_plate_number: int):
        if floor(log10(license_plate_number)) + 1  != 7:
            print(f"Digit number validation for license plate number {license_plate_number} failed")
        self.number = license_plate_number

    def park(self, parking_lot: ParkingLot, spot_num: int):
        try:
            if parking_lot.lot[spot_num] == -1:
                parking_lot.lot[spot_num] = self.number
                parking_lot.inc_parked_num()
                return True, f"The car with license plate {self.number} parked successfully at {spot_num}."
            else:
                return False, (f"The car with license plate {self.number} was not parked successfully because another "
                               f"car is already parked at {spot_num}.")
        except IndexError:
            return False, f"The Spot# {spot_num} does not exist."

    def __str__(self):
        return str(self.number)
