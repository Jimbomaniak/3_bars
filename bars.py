import json
from geopy.distance import great_circle


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_biggest_bar(data):
    barnames_seatscount = {bar['Cells']['Name']:bar['Cells']['SeatsCount'] for bar in data}
    biggest_bar = max(barnames_seatscount, key=barnames_seatscount.get)
    return biggest_bar


def get_smallest_bar(data):
    barnames_seatscount = {bar['Cells']['Name']:bar['Cells']['SeatsCount'] for bar in data}
    smallest_bar = min(barnames_seatscount, key=barnames_seatscount.get)
    return smallest_bar


def get_closest_bar(data, user_coordinates):
    all_bar_distances = {}
    for bar in data:
        bar_coordinates = bar['Cells']['geoData']['coordinates']
        bar_name = bar['Cells']['Name']
        distance = great_circle(user_coordinates, bar_coordinates).kilometers
        all_bar_distances[bar_name] = distance
    closest_bar = min(all_bar_distances, key=all_bar_distances.get)
    return closest_bar


def get_coordinates():
    try:
        longitude = float(input('Write longitude (example:23.1113): '))
        latitude = float(input('Write latitude (example:23.1113): '))
        user_coordinates = [longitude, latitude]
        return user_coordinates
    except ValueError:
        print('Enter digits only')
        return get_coordinates()


def get_distance_to_bar(bar_coordinates, user_coordinates):
    user_long, user_lat = user_coordinates
    bar_long, bar_lat = bar_coordinates
    distance_to_bar = sum([abs(bar_long - user_long), abs(bar_lat - user_lat)])
    return distance_to_bar


if __name__ == '__main__':
    filepath = input('Path to json file(e.g. /c:/users/bars.json): ')
    data = load_data(filepath)
    print('The biggest bar is: {0}'.format(get_biggest_bar(data)))
    print('The smallest bar is: {0}'.format(get_smallest_bar(data)))
    user_coordinates = get_coordinates()
    print('The closest bar is: {0}'.format(get_closest_bar(data, user_coordinates)))
