import haravasto as hav
import ikkunasto as iku
import random as ran
import time
import copy
import json

hiiri = {
    1: 'vasen',
    2: 'keski',
    4: 'oikea' 
}

liput = {
    'jatka': True,
    "peli": False,
    "voitto": 0,
    'save': False
}

peli = {
    "leveys": 0,
    "korkeus": 0,
    "miinat": 0,
    "miinakrd": [],
    "liputetut": 0,
    "start": 0
}

kentta = {
    "alue": [],
    "tarkistus": []
}

stats = {
    'nimi': 'Tyhjä',
    'liputetut': 0,
    'aika': 0
}

data ={
    'tilasto': []
}

def main():
    menu()
    pelin_alku()


def menu():
    '''Terminaalissa toimiva mainmenu'''
    print('Tervetuloa Miinaharavaan! Valitse toiminto.')
    while True:
        print('(P)elaa')
        print('(T)ulokset')
        print('(S)ulje')
        valinta = input('').lower()
        if valinta == 'p':
            liput['pelaa'] = True
        elif valinta == 't':
            tulokset()
        elif valinta == 's':
            liput['jatka'] == False
        else:
            print('Komentoa ei tunnistettu')

def arvot():
    '''Pyytää arvoja miinaharavalle'''
    valinta = input('(S)yötä arvot tai (Y)lläty').lower()
    if valinta == 's'
        while peli['leveys'] < 5:
            try:
                peli['leveys'] = int(input('Syötä kentän leveys (min 5): '))
            except ValueError:
                print('Leveyden täytyy olla numero')

        while peli['korkeus'] < 5:
            try:
                peli['korkeus'] = int(input('Syötä kentän pituus (min 5): '))
            except ValueError:
                print('Pituuden täytyy olla numero')

        while peli['miinat'] <= 0:
            try:
                peli['miinat'] = int(input('Anna miinojen määrä: '))
            except ValueError:
                print('Miinojen lukumäärän täytyy olla numero')
    
    else:
        yllata()


def yllata():
    '''Yllättää pelaajan'''
    peli['korkeus'] = ran.randint(5, 15)
    peli['leveys'] = ran.randint(5, 15)
    pelialue = peli['korkeus'] * peli['leveys']
    miina_ala = int(pelialue / ran.randint(5, 6))
    miina_yla = int(pelialue / ran.randint(4, 5))
    peli['miinat'] = ran.randint(miina_ala, miina_yla)


def luo_kentta(alue, korkeus, leveys):
    '''Luo kentän pelaajalle'''
    for rivi in range(korkeus):
        alue.append([])
        for sarake in range(leveys):
            alue[-1].append(' ')
    
    jaljella = []
    for x in range(leveys):
        for y in range(korkeus):
            jaljella.append((x, y))

    for i in range(peli{'miinat'}):
        krd = ran.choice(jaljella)
        alue[krd[1]krd[0] = 'x'
        peli['miinakrd'].append(krd)
        vapaa.remove(krd)
    
    kentta['tarkistus'] = copy.deepcopy(kentta)


def aloita_peli():
    peli['miinakrd'] = []
    liput['peli'] = False
    liput['voitto'] = 0
    peli['liputetut'] = 0
    liput



    

if __name__ == "__main__":
    pelin_alku()
