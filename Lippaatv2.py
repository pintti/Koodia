'''Ohjelma joka huolehtii ampusien vaikutuksesta lippaisiin sekä niiden lataamisesta'''

LIPPAAT = {
    "1": 30,
    "2": 30,
    "3": 30,
    "4": 0,
    "5": 0,
    "6": 0
}

def ammu(kirja, lipas, lk_mär):
    '''Aseella ampumista hallinnoiva funktio. kirja on lippaiden kirjasto, lipas on lippaan numero 
    ja lk_mär on laukausten määrä. Muokkaa lipas sanakirjaa ammuttujen ammusten määrän verran.'''
    for i in range(lk_mär):
            kirja[str(lipas)] -= 1
            if kirja[str(lipas)] <= 0:
                print('Klik!')
                break
            elif i < (lk_mär-1):
                print(kirja[str(lipas)])

def lataa(kirja, lipas):
    '''Aseen lataamista ja lippaissa olevien ammuksien hallitseva funktio,
    paluttaa lippaan jossa on vielä panoksia tai jos kaikki panokset ovat loppu
    palauttaa ensimmäisen lippaan ja kertoo panosten olevan loppu'''
    lipas += 1
    if kirja[str(lipas)] == 0:
        for i in range(1, 7):
            if kirja[str(i)] > 0:
                lipas = i
                return lipas
        lipas = 1
        print('Ammukset loppu!')
        return lipas
    else:
        return lipas
        

def main(kirja):
    '''Aseen käyttöä hallinnoiva funktio, kirja on aseessa olevat lippaat sanakirjassa'''
    lipas = 1
    while True:
        if kirja[str(lipas)] <= 0:
            kirja[str(lipas)] = 0
        print(kirja[str(lipas)])
        print('(A)mmu a:ta käyttämällä tai (l)ataa ase.')
        kaytto = list(input(''.lower()))
        if kaytto[0] == 'a':
            ammu(kirja, lipas, len(kaytto))
        elif kaytto[0] == 'l':
            lipas = lataa(kirja, lipas)
            

        
if __name__ == "__main__":
    main(LIPPAAT)
