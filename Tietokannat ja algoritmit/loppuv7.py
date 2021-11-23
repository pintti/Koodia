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


def solve_graph(graph):
    start = 1
    end = int(graph.end_city)
    
    cities_list = [city for city in graph.city_list]
    graph.heights[start] = 0


    now_city = 0
    last_city = 0
    while cities_list:
        minval = INF
        for city in cities_list:
            if graph.heights[city] < minval and graph.heights[city] != 0:
                minval = graph.heights[city]
                now_city = city
        print(now_city)
        print(minval)
        cities_list.remove(now_city)
        
        for next_city in graph.next_city_list[now_city]:
            city_number = next_city.next_city
            if graph.heights[city_number] > minval:
                graph.heights[city_number] = next_city.city_height
                graph.routes[city_number] = now_city
        print(graph.heights)
        print(graph.routes)
        last_city = now_city
        input()
        

        if now_city == end:

            break

    return graph


def solve_route(graph):
    route = []
    start = graph.end_city
    height = 0
    while start != 1:
        route.insert(0, start)
        start = graph.routes[start]
        if graph.heights[start] > height:
            height = graph.heights[start]
    route.insert(0, start)
    return route, height



if __name__ == "__main__":
    text = open_file()
    now = time.time()
    graph = open_text(text)
    graph = solve_graph(graph)
    
    #route, height = solve_route(graph)
    #print("Your route", route, "and max height", height)
    #print(maximum_height)