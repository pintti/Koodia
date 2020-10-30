library = {
    "nmbr_of_cities": 0,
    "nmbr_of_roads": 0,
    "end_city": 0,
    'cities': {}
}

memory = {
    'road_taken': [],
    'road_to_think': []
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


def count_roads(cities, start):
    next_city, next_height = cities[start][0]
    memory['road_to_think'] = cities[start][1]
    while start != 1:
        memory['road_taken'] = [start]
        for city, height in cities[start]:
            if height < next_height:
                next_city = city
                next_height = height
            elif memory['road_to_think'][1] < height:
                memory['road_to_think'] = (city, height)
        if next_city not in memory['road_taken']:
            start = next_city
        else:
            


if __name__ == "__main__":
    text = open_file("text.txt")
    check_lines(text)
    count_roads(library['cities'], str(library['end_city']))
