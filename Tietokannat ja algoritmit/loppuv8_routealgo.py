import time

INF = float('inf')

class City:
    def __init__(self, city, height):
        self.next_city = city
        self.city_height = height
        self.last_city = 0

class Graafi:
    def __init__(self, nmbr_of_cities, end_city, text):
        self.cities = nmbr_of_cities
        self.end_city = end_city
        self.next_city_list = {}
        self.city_list = []

        self.heights = {}
        self.routes = {}

        for i in range(1, nmbr_of_cities+1):
            self.next_city_list[i] = []
            self.city_list.append(i)
            self.heights[i] = INF
            self.routes[i] = 0


        for now_city, next_city, height in text:
            add_city(self, int(now_city), int(next_city), int(height))

    
def add_city(cclass, city, next_city, height):
    cclass.next_city_list[city].append(City(next_city, height))
    cclass.next_city_list[next_city].append(City(city, height))
        

def open_file():
    """"Opens file, cleans up the newlines from text and returns the text for further
    work"""
    while True:
        try:
            file = input("Please input the file: ")
            #file = "graph_testdata/graph_ADS2018_20.txt"
            with open(file, "r") as f:
                text = f.readlines()
                for i, line in enumerate(text):
                    text[i] = line.strip().split(' ')
            return text
        except FileNotFoundError:
            print('Such file does not exist.')
    

def open_text(text):
    nmbr_of_cities, roads = text.pop(0)
    endcity = int(text[-1][0])
    text.pop(-1)
    cities = Graafi(int(nmbr_of_cities), endcity, text)
    return cities


def solve_height(graph):
    start = 1
    end = int(graph.end_city)
    
    cities_list = [city for city in graph.city_list]
    graph.heights[start] = 0

    city = cities_list[0]

    while cities_list:
        minval = INF
        for next_city in cities_list:
            if graph.heights[next_city] < minval:
                minval = graph.heights[next_city]
                city = next_city
        cities_list.remove(city)

        for next_city in graph.next_city_list[city]:
            number = next_city.next_city
            if graph.heights[number] > minval:
                if graph.heights[number] < next_city.city_height:
                    pass
                elif next_city.city_height > minval:
                    graph.heights[number] = next_city.city_height
                    graph.routes[number] = city
                else:
                    graph.heights[number] = minval
                    graph.routes[number] = city
                #graph.routes[number] = city
        if city == end:
            break
    return graph


def solve_route(graph, height):
    city_list = [1]
    
    while city_list:
        second_list = []
        for city in city_list:
            for adj_city in graph.next_city_list[city]:
                if adj_city.city_height <= height:
                    second_list.append(adj_city.next_city) 

        




if __name__ == "__main__":
    text = open_file()
    now = time.time()
    graph = open_text(text)
    now = time.time()
    graph = solve_height(graph)
    end = time.time()
    
    height = graph.heights[graph.end_city]
    print(height)

    """route, height = solve_route(graph)
    print("Your route", route, "and max height", height)
    print("Time taken:", end-now)
    #print(maximum_height)"""