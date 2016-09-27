import json


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        data = json.load(file)
    return data 


def get_biggest_bar(data):
    res = {data[x]['Cells']['Name']:data[x]['Cells']['SeatsCount'] for x in range(0,len(data))}
    name = max(res, key=res.get)
    return name


def get_smallest_bar(data):
    res = {data[x]['Cells']['Name']:data[x]['Cells']['SeatsCount'] for x in range(0,len(data))}
    name = min(res, key=res.get)
    return name


def get_closest_bar(data, longitude, latitude):
    res = {data[x]['Cells']['Name']:
sum([abs(
        abs(data[x]['Cells']['geoData']['coordinates'][0]) - abs(longitude)
        ),
    abs(
        abs(data[x]['Cells']['geoData']['coordinates'][1]) - abs(latitude)
        )
    ]) for x in range(0,len(data))}
    name = min(res, key=res.get)
    return name


if __name__ == '__main__':
    print(get_biggest_bar(load_data('бары.json')))
    print(get_smallest_bar(load_data('бары.json')))
    longitude = float(input('Введите долготу, пример 24.12444'))
    latitude = float(input('Введите широту, пример 24.12444'))
    print(get_closest_bar(load_data('бары.json'), longitude, latitude))
