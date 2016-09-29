import json


def load_data():
    filepath = input('Write your path to directory with json file(like c:/users/bars.json): ')
    try:
        with open(filepath, encoding='utf-8') as file:
            data = json.load(file)
        return data 
    except FileNotFoundError:
        print('No such file in directory')
        return load_data()


def get_biggest_bar(data):
    res = {data['Cells']['Name']:data['Cells']['SeatsCount'] for data in data}
    biggest_bar = max(res, key=res.get)
    return biggest_bar


def get_smallest_bar(data):
    res = {data['Cells']['Name']:data['Cells']['SeatsCount'] for data in data}
    smallest_bar = min(res, key=res.get)
    return smallest_bar


def get_closest_bar(data):
    user_coordinates = get_coordinates()
    all_distances_to_bars = {bar['Cells']['Name']:get_distance_to_bar(bar['Cells']['geoData']['coordinates'],user_coordinates) for bar in data}
    closest_bar = min(all_distances_to_bars, key=all_distances_to_bars.get)
    return closest_bar

def get_coordinates():
    try:
        longitude = float(input('Write longitude (example:23.1113): '))
        latitude = float(input('Write latitude (example:23.1113): '))
        user_coordinates = [longitude, latitude]
        return user_coordinates
    except ValueError:
        print('Write only integers')
        return get_coordinates()
        
def get_distance_to_bar(bar_coordinates, user_coordinates):
    user_long, user_lat = user_coordinates
    bar_long , bar_lat = bar_coordinates
    distance_to_bar = sum([abs(bar_long - user_long),abs(bar_lat - user_lat)])
    return distance_to_bar




if __name__ == '__main__':
    data = load_data()
    print('The biggest bar is: {0}'.format(get_biggest_bar(data)))
    print('The smallest bar is: {0}'.format(get_smallest_bar(data)))
    print('The closest bar to you is: {0}'.format(get_closest_bar(data)))
