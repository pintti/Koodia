import random
import os

def start_game():
    players = {}
    print('Lisää pelaajan nimi tai tyhjä lopettaaksesi:')
    while True:
        pname = input()
        if pname:
            players[pname] = dict(wins=0,position=0,streak=0,losses=0)
        else:
            os.system('cls')
            return players


def game_loop(players, pos_list):
    while True:
            for player in players:
                player_pos = players[player]['position']
                pos_list[player_pos-1] = player
            print("POS  NAME       WINS      STREAK     LOSSES")
            for pos_player in pos_list:
                print(f'{players[pos_player]["position"]:<4} {pos_player:<8}{players[pos_player]["wins"]:>4}{players[pos_player]["streak"]:>10}{players[pos_player]["losses"]:>11}')
            try:
                win_num = input("Voittajan numero: ")
                if 0<int(win_num)<5:
                    players = score(players, int(win_num))
                else:
                    players = skip(players, int(win_num))
                os.system('cls')
            except:
                if "dnf" in win_num:
                    _, dnf_p = win_num.split()
                    print(dnf_p)
                    del pos_list[players[dnf_p]["position"]-1]
                    del players[dnf_p]
                    os.system('cls')
                elif "exit" == win_num:
                    return
                else:
                    os.system('cls')
                    print("KÄYTTÖ\nVoitto: laita pelaajan numero joka voitti (välillä 1-4)\nSKIP: laita skippaavan pelaajan numeron eteen miinusmerkki (esim. -3)\nDNF: kirjoita dnf ja poistuvan pelaajan nimi")


def score(players, win_num):
    for player in players:
        if players[player]["position"] == win_num:
            players[player]["position"] = len(players)
            players[player]["wins"] += 1
            players[player]["streak"] = 0
        elif players[player]["position"] <= 4:
            players[player]["streak"] += 1
            players[player]["losses"] += 1
        else:
            if players[player]["position"] != 5:
                players[player]["position"] -=1
            else:
                players[player]["position"] = win_num
    return players


def skip(players, win_num):
    skip_num = -win_num
    for player in players:
        if players[player]["position"] == skip_num:
            players[player]["position"] = len(players)
        elif players[player]["position"] > 4:
            if players[player]["position"] != 5:
                players[player]["position"] -= 1
            else:
                players[player]["position"] = skip_num
    return players
               

def give_pos(plist):
    numlist = []
    pos_list = []
    for i in range(1, len(plist)+1):
        numlist.append(i)
        pos_list.append(" ")
    for player in plist:
        num = random.choice(numlist)
        numlist.remove(num)
        plist[player]["position"] = num
    return plist, pos_list


def main():
    plist = start_game()
    plist, post_list = give_pos(plist)
    game_loop(plist, post_list)

main()


