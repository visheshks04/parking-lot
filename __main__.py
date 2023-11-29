from Car import Car
from ParkingLot import ParkingLot

import random

PARKING_LOT_AREA = 2000

plate_nums = list(map(int, input("Please input the number plates array, space seperated: ").split()))
parking_lot = ParkingLot(PARKING_LOT_AREA)

i = len(plate_nums)-1
while len(plate_nums) > 0:
    car = Car(plate_nums[i])
    parked, message = car.park(parking_lot, random.randint(0, parking_lot.get_lot_length()-1))
    print(message)
    if not parked:
        continue

    plate_nums.pop(i)
    i -= 1

    if parking_lot.is_full():
        break


parking_lot.get_json_data()