library = {
    "nmbr_of_cities": 0,
    "nmbr_of_roads": 0,
    "end_city": 0,
    'cities': {}
}


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
    for line in text:
        try:
            city, neighbour, height = line
            create_city(int(city), int(neighbour), int(height))
        except ValueError:
            print("City values not usable")


def create_city(city, neighbour, road_height):
    """Functions creates cities in the library"""
    if str(city) not in library['cities'].keys():
        library['cities'][str(city)] = []
    if str(neighbour) not in library['cities'].keys():
        library['cities'][str(neighbour)] = []
    library['cities'][str(city)].append((neighbour, road_height))
    library['cities'][str(neighbour)].append((city, road_height))


def range_check(cities, city, n=0, checked_cities=None):
    """Function checks the range to goal"""
    if checked_cities == None:
        checked_cities = []
    ranges = []
    if city == 1:
        return n
    for next_city, _ in cities[str(city)]:
        if next_city == 1:
            return n+1
        elif next_city not in checked_cities:
            checked_cities.append(next_city)
            nest = range_check(cities, next_city, n+1, checked_cities)
            if nest:
                ranges.append(nest)
    checked_cities = []
    if ranges:
        return min(ranges)


def find_road(cities):
    """This is where the magic happens"""
    roads = []
    city = library['end_city']
    for next_city, next_road in cities[str(city)]:
        roads.append([city, next_city, next_road])
    while city != 1:
        index = find_small(roads)
        future = roads[index]
        future.pop(-1)
        del roads[index]
        for next_city, next_road in cities[str(future[-1])]:
            if next_city not in future:
                new_road = future + [next_city, next_road]
                roads.append(new_road)
        city = future[-1]
    return future


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


def turn_road(old_road):
    fixed_road = []
    for i in range(len(old_road)):
        fixed_road.append(old_road[-1-i])
    return fixed_road


def find_peak(cities, road):
    try:
        i = 1
        peak = None
        for number in road:
            for value in cities[str(number)]:
                if value[0] == road[i]:
                    if not peak:
                        peak = value[1]
                    elif peak < value[1]:
                        peak = value[1]
                i += 1
    except IndexError:
        return peak


def print_road(road, peak):
    print("Your road is through cities", end=' ')
    print(*road, sep=', ', end=' ')
    print('with max height of', peak, end=' m.')


if __name__ == "__main__":
    text = open_file()
    check_lines(text)
    if range_check(library['cities'], library['end_city']):
        inv_road = find_road(library['cities'])
        real_road = turn_road(inv_road)
        peak = find_peak(library['cities'], real_road)
        print_road(real_road, peak)
    else:
        print('No roads to destination available.')