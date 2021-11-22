import time

INF = float('inf')

class City:
    """Luokka johon tallennetaan seuraava kaupunki sekä näiden kahden kaupungin välisen reitin korkeus.
    next_city = Seuraavan kaupunhin numero
    city_height = Tien korkeus"""                                            
    def __init__(self, city, height):
        self.next_city = city
        self.city_height = height


class Graafi:
    """Graafi jossa on tallennettuna kapupungit, maali sekä listat kaupungeista että niiden viereisistä kaupungeista.
    cities = Kaupunkien lukumäärä
    end_city = Maali
    next_city_list = Indeksoitu sanakirja jossa jokainen indeksi osoittaa tiettyä kaupunkia. 
    Tässä indeksissä on tallennettuna lista kaupungin viereisistä kaupungeista City-luokkana.
    city_list = Lista kaupungeista.
    heights = Indeksoitu lista korkeuksista.
    routes = Indeksoitu lista mistä kaupungista on kuljettu kyseiseen kaupunkiin."""
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
    """Solves the graph using a modified version of Djikstras algorithm."""
    start = 1
    end = int(graph.end_city)
    
    cities_list = [city for city in graph.city_list]
    graph.heights[start] = 0

    city = cities_list[0]

    while cities_list:  #Loop as long as cities_list has objects.
        minval = INF
        for next_city in cities_list:   #Find the route with smallest value, pick the city with smallest route as observed
            if graph.heights[next_city] < minval:
                minval = graph.heights[next_city]
                city = next_city
        try:
            cities_list.remove(city)       #Remove checked city so no useless looping will happen.
        except ValueError:
            print("Route not available.")
            return 0

        for next_city in graph.next_city_list[city]:    #Assing values to the cities next to the observed city.
            number = next_city.next_city
            if graph.heights[number] > max(minval, next_city.city_height):
                graph.heights[number] = max(minval, next_city.city_height)
                graph.routes[number] = city
                """
                if graph.heights[number] < next_city.city_height: #This is so that cities with smaller values don't get replaced by bigger values.
                    pass
                elif next_city.city_height > minval:    #This replaces  INFs and values that are too high with smaller values.
                    graph.heights[number] = next_city.city_height
                    graph.routes[number] = city
                else:                                   #Else keep the minval value assigned so that we can always access it fast by checking the value the goal got.
                    graph.heights[number] = minval
                    graph.routes[number] = city"""
        if city == end:
            return graph


def solve_route(graph):
    """This merely checks the route from end to start and readies it for printing."""
    route = []
    start = graph.end_city
    height = graph.heights[start]
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
    now = time.time()
    graph = solve_graph(graph)
    end = time.time()

    if graph:
        route, height = solve_route(graph)
        print("Your route", route, "and max height", height)
        print("Time taken:", end-now)