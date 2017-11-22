import requests
from geopy.distance import vincenty as calc_distance
import argparse


class Bar:

    def __init__(self, raw_bar_obj):
        self.name = raw_bar_obj["properties"]["Attributes"]["Name"]
        self.seats_count = (raw_bar_obj['properties']['Attributes']
                            ['SeatsCount'])
        self.longitude = raw_bar_obj['geometry']['coordinates'][0]
        self.latitude = raw_bar_obj['geometry']['coordinates'][1]
        self.address = raw_bar_obj['properties']['Attributes']['Address']
        self.phone_number = (raw_bar_obj['properties']['Attributes']
                             ['PublicPhone'][0]["PublicPhone"])

    def __str__(self):
        return '"{name}":\n\t{addr}\n\tТел.: +7{tel}'.format(
            name=self.name, addr=self.address, tel=self.phone_number)

    def calc_distance_to_certain_point(self, point_longitude, point_latitude):
        distance = calc_distance((self.longitude, self.latitude),
                                 (point_longitude, point_latitude)).kilometers
        return distance


def load_api_key(api_key_file_path):
    with open(api_key_file_path) as file:
        api_key = file.read().rstrip()
        return api_key


def get_arguments_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_api', help='path to file with api-key')
    parser.add_argument('longitude', type=float,
                        help='longitude of users current location')
    parser.add_argument('latitude', type=float,
                        help='latitude of users current location')
    return parser


def load_data(api_key):
    request_params = {'api_key': api_key}
    request = requests.get('https://apidata.mos.ru/v1/datasets/1796/features',
                           params=request_params)
    raw_data = request.json()
    return raw_data


def get_list_of_bars(raw_data):
    list_of_bars = [Bar(raw_bar_obj) for raw_bar_obj
                    in raw_data["features"]]
    return list_of_bars


def get_biggest_bar(list_of_bars):
    biggest_bar = max(list_of_bars, key=lambda bar: bar.seats_count)
    return biggest_bar


def get_smallest_bar(list_of_bars):
    smallest_bar = min(list_of_bars, key=lambda bar: bar.seats_count)
    return smallest_bar


def get_closest_bar(list_of_bars, user_longitude, user_latitude):
    closest_bar = min(list_of_bars,
                      key=lambda bar:
                      bar.calc_distance_to_certain_point(user_longitude,
                                                         user_latitude))
    return closest_bar


if __name__ == '__main__':
    arguments_parser = get_arguments_parser()
    arguments = arguments_parser.parse_args()
    user_longitude, user_latitude = arguments.longitude, arguments.latitude
    path_to_api_file = arguments.path_to_api

    api_key = load_api_key(path_to_api_file)
    bars_raw_data = load_data(api_key)
    list_of_bars = get_list_of_bars(bars_raw_data)

    smallest_bar = get_smallest_bar(list_of_bars)
    biggest_bar = get_biggest_bar(list_of_bars)
    closest_bar = get_closest_bar(list_of_bars, user_longitude, user_latitude)

    print('* The smallest bar in Moscow is {}\n'.format(smallest_bar))
    print('* The biggest bar in Moscow is {}\n'.format(biggest_bar))
    print('* The closest bar for you is {}\n'.format(closest_bar))
