import random

def take_names():
    names = []
    while True:
        name = input('Player name, blank to ready: ')
        if name == '':
            return names
        elif name in names:
            print('Name in use.')
        else:
            names.append(name)


def shuffle(g_players, names):
    brackets = len(names) // g_players
    left_overs = len(names) % g_players
    bracket_list = []
    for i in range(brackets):
        bracket_list.append(create_bracket(names, g_players))
    if left_overs > 0:
        bracket_list.append(create_bracket(names, left_overs))
    return bracket_list


def create_bracket(name_list, g_players):
    bracket = []
    for i in range(g_players):
        bracket.append(name_list.pop(random.randint(0, len(name_list)-1)))
    return bracket


def main():  
    g_players = int(input('Players per game: '))     
    names = take_names()                            
    bracket_list = shuffle(g_players, names)    
    print("Brackets:")
    for i in range(len(bracket_list)):
        print(bracket_list[i])                


if __name__ == "__main__":
    main()