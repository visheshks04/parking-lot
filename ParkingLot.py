import json
from S3Service import S3Service

import os


class ParkingLot:
    def __init__(self, square_footage_size, parking_spot_size=(8, 12)):
        self.square_footage_size = square_footage_size
        self.parking_spot_size = parking_spot_size
        self.parking_spot_area = parking_spot_size[0] * parking_spot_size[1]
        self.n_cars = self.square_footage_size // self.parking_spot_area
        self.lot = [-1] * self.n_cars
        self.parked_num = 0

    def get_lot_length(self):
        return len(self.lot)

    def inc_parked_num(self):
        self.parked_num += 1

    def is_full(self):
        return self.parked_num == len(self.lot)

    def get_json_data(self):
        json_data = dict()

        for i, spot in enumerate(self.lot):
            if spot != -1:
                json_data[spot] = i

        print(json_data)

        with open('parking_lot.json', 'w') as outfile:
            json.dump(json_data, outfile)

        bucket_name = os.environ['bucket_name']
        aws_access_key = os.environ['aws_access_key']
        aws_secret_key = os.environ['aws_secret_key']

        s3_service = S3Service(bucket_name, aws_access_key, aws_secret_key)
        s3_service.save('parking_lot.json')
