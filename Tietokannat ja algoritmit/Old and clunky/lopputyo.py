library = {
    "nmbr_of_cities": 0,
    "nmbr_of_roads": 0,
    "end_city": 0,
    'cities': {}
}

memory = {
    'road_taken': [],
    'road_to_think': [],
    'highest_road_taken': 0,
    'steps': 0,
    'dont': [],
    'second': [], 
    'true_road': []
}


def open_file(file):
    """"Opens file, cleans up the newlines from text and returns the text for further
    work"""
    while True:
        try:
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
    if str(city) not in library['cities'].keys():
        library['cities'][str(city)] = []
    if str(neighbour) not in library['cities'].keys():
        library['cities'][str(neighbour)] = []
    library['cities'][str(city)].append((neighbour, road_height))
    library['cities'][str(neighbour)].append((city, road_height))


def pretty_printer(printed):
    for value in printed:
        print(value, end=': ')
        print(printed[value][0], printed[value][1])


def first_step(cities, start):
    memory['road_taken'].append(int(start))
    city, road = cities[start][0]
    for next_city, next_road in cities[start]:
        if road < next_road:
            next_city, next_road = city, road
        else:
            if not memory['second']:
                memory['second'] = (next_city, next_road)
            elif memory['second'][1] > next_road:
                memory['second'] = (next_city, next_road, memory['steps'])
    memory['highest_road_taken'] = next_road
    count_roads(cities, next_city, range_check(cities, next_city, 0), int(start))


def count_roads(cities, start, n, last_city=0):
    memory['road_taken'].append(start)
    memory['steps'] += 1
    print('START ', start)
    print(memory['highest_road_taken'])
    if start != 1:
        next_road = 1000
        print(cities[str(start)])
        for city, road in cities[str(start)]:
            if city != last_city and city not in memory['dont']:
                print(city, road)
                if road <= memory['highest_road_taken'] and road < next_road:
                    """nu_n = range_check(cities, city)
                    if nu_n <= n:
                        n = nu_n
                        next_city, next_road = city, road"""
                    next_city, next_road = city, road
                #elif road < next_road:
                #    next_city, next_road = city, road
                elif not memory['second']:
                    memory['second'] = (city, road, memory['steps'])
                elif memory['second'][1] > road:
                    memory['second'] = (city, road, memory['steps'])
        print(memory['second'])
        if next_road > memory['highest_road_taken']:
            memory['highest_road_taken'] = next_road
        if memory['second']:
            if next_road > memory['second'][1]:
                for i in range(memory['second'][2], memory['steps']):
                    memory['dont'].append(memory['road_taken'].pop(-1))
                next_city = memory['road_taken'].pop(-1)
                memory['steps'] = memory['steps'] - memory['second'][2]
                memory['highest_road_taken'] = memory['second'][1]
                memory['second'] = []
                count_roads(cities, next_city, range_check(cities, next_city))
            else:
                count_roads(cities, next_city, range_check(cities, next_city), start)
        else:
            count_roads(cities, next_city, range_check(cities, next_city), start)



def range_check(cities, city, n=0, checked_cities=None):
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



def turn_road(old_road, fixed_road):
    for value in range(len(old_road)):
        fixed_road.append(old_road[-1+value])
    


if __name__ == "__main__":
    text = open_file("text.txt")
    check_lines(text)
    if range_check(library['cities'], library['end_city']):
        first_step(library['cities'], str(library['end_city']))
        turn_road(memory['road_taken'], memory['true_road'])
        print(memory['true_road'], memory['highest_road_taken'])
    else:
        print('No roads to destination available.')