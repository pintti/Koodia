import time

library = {
    "nmbr_of_cities": 0,
    "nmbr_of_roads": 0,
    "end_city": 0,
    'forced': 0,
    'steps': [],
    'cities': {}
}

now = 0

def open_file():
    """"Opens file, cleans up the newlines from text and returns the text for further
    work"""
    while True:
        try:
            file = input("Please input the file: ")
            with open(file, "r") as f:
                text = f.readlines()
                for i, line in enumerate(text):
                    text[i] = line.strip().split(' ')
            return text
        except FileNotFoundError:
            print('Such file does not exist.')
    

def check_lines(text):
    """Function checks that lines are right and inputs them into library"""
    cities, roads = text.pop(0)
    library["nmbr_of_cities"], library["nmbr_of_roads"] = int(cities), int(roads)
    library["end_city"] = int(text.pop(-1)[0])
    for number in range(1, library['nmbr_of_cities'] + 1):
        library['cities'][str(number)] = []
    for line in text:
        try:
            city, neighbour, height = line
            create_city(int(city), int(neighbour), int(height))
        except ValueError:
            print("City values not usable")


def create_city(city, neighbour, road_height):
    """Functions creates cities in the library"""
    library['cities'][str(city)].append((neighbour, road_height))
    library['cities'][str(neighbour)].append((city, road_height))


def range_check(cities, city, upper_road=1000):
    try:
        old_n = 0
        checked_cities = [city]
        checking_cities = [city]
        while checking_cities:
            a = 0
            for next_city, road in cities[str(city)]:
                if road <= upper_road:
                    if next_city == library['end_city']:
                        return old_n + 1
                    else:
                        if next_city not in checked_cities:
                            checking_cities.append(next_city)
                    a += 1
            checked_cities.append(checking_cities[-1])
            city = checking_cities.pop(-1)
            if a > 0:
                old_n += 1
    except ValueError:
        return False  


def find_road(cities):
    """This is where the magic happens"""
    roads = []
    city = 1
    for next_city, next_road in cities[str(city)]:
        roads.append([city, next_city, next_road])
    while city != library['end_city']:
        index = find_small(roads)
        future = roads.pop(index)
        old_road = future.pop(-1)
        if old_road < library['forced']:
            old_road = library['forced']
        for next_city, next_road in cities[str(future[-1])]:
            if next_city not in future:
                if old_road >= next_road:                            # Testing show that this spaghetti here makes the code 20% more efficient. HOW?
                    roads.append(future + [next_city, old_road])
                else:
                    roads.append(future + [next_city, next_road])
        city = future[-1]
        print(future)
    print(future, old_road)
    print(time.time() - now)
    future = correct_road(cities, old_road)
    return future, old_road


def correct_road(cities, tallest_road):
    """No actually it's here"""
    city = 1
    road = [city]
    cancel_tiles = []
    while city != library['end_city']:
        fastest_route = []
        for next_city, next_road in cities[str(city)]:
            if next_city not in road and next_city not in cancel_tiles:
                if tallest_road >= next_road:
                    fastest_route.append([next_city, range_check(cities, next_city, tallest_road)])
        if fastest_route:
            index = find_small(fastest_route)
            city = (fastest_route[index][0])
            road.append(city)
        else:
            cancel_tiles.append(road.pop(-1))
            city = road[-1]
    return road


def find_forced(cities):
    forced_1 = 1000
    forced_end = 1000
    for city, road in cities["1"]:
        if road < forced_1:
            forced_1 = road
    for city, road in cities[str(library['end_city'])]:
        if road < forced_end:
            forced_end = road
    if forced_1 > forced_end:
        library['forced'] = forced_1
    else:
        library['forced'] = forced_end


def find_small(roads):
    small = None
    for value in roads:
        if small:
            if value[-1] < small:
                small = value[-1]
                index = roads.index(value)
        else:
            small = value[-1]
            index = roads.index(value)
    return index


def print_road(road, peak):
    print("Your road is through cities", end=' ')
    print(*road, sep=', ', end=' ')
    print('with max height of', peak, 'm')


if __name__ == "__main__":
    text = open_file()
    now = time.time()
    check_lines(text)
    if range_check(library['cities'], 1):
        find_forced(library['cities'])
        real_road, peak = find_road(library['cities'])
        print_road(real_road, peak)
        print(time.time() - now)
    else:
        print('No roads to destination available.')