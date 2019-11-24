'''Moduuli luo päävalikon pelille, päävalikkoon sisältyy pelin
aloittaminen jossa pelaaja voi säätää haluamansa dimensiot että miinojen
määrä, katsella tilastoja, että sulkea ohjelman'''

import haravasto as hav
import ikkunasto as iku
import random as ran
import time

hiiri = {
    1: 'vasen',
    2: 'keski',
    4: 'oikea' 
}

elementit = {
    "kehys1": None,
    "teksti1": None,
    "kehys2": None,
    "teksti2": None,
    "korkeus": None,
    "leveys": None
}

peli = {
    "leveys": 5,
    "korkeus": 5,
    "miinat": None,
    "jaljella": []
}

kentta = {
    "alue": []
}

def aloita_peli():
    '''Funktio kysyy pelaajalta kentän koon sekä miinojen määrän sekä
    palauttaa nämä arvot. Avataan ali-ikkunaan jonne syötetään kentan
    leveys, korkeus sekä miinojen määrä (ei implementoitu vielä).'''
    ala = iku.luo_ali_ikkuna('')
    ala_kehys1 = iku.luo_kehys(ala, iku.YLA)
    ala_kehys2 = iku.luo_kehys(ala)
    ala_teksti1 = iku.luo_tekstilaatikko(ala_kehys1, 20, 1)
    iku.kirjoita_tekstilaatikkoon(ala_teksti1, "Anna kentän korkeus")
    elementit["korkeus"] = iku.luo_tekstikentta(ala_kehys1)
    ala_teksti2 = iku.luo_tekstilaatikko(ala_kehys2, 20, 1)
    iku.kirjoita_tekstilaatikkoon(ala_teksti2, "Anna kentän leveys")
    elementit["leveys"] = iku.luo_tekstikentta(ala_kehys2)
    iku.luo_nappi(ala_kehys2, 'Syötä arvot ja aloita peli', arvo_kasittelija)
    iku.luo_nappi(ala_kehys2, 'Yllätä minut', yllata)
    

def arvo_kasittelija():
    '''Funktio hakee ja tarkistaa pelaajan antaman arvon. Kentta on
    tekstikenttä johon käyttäjä kirjoittaa, teksti alue johon kirjoitetaan
    tekstiä.'''
    try:
        peli["korkeus"] = int(iku.lue_kentan_sisalto(elementit["korkeus"]))
        peli["leveys"] = int(iku.lue_kentan_sisalto(elementit["leveys"]))
        if peli["korkeus"] <= 0 or peli["leveys"] <= 0:
            iku.avaa_viesti_ikkuna("Virhe", "Arvojen täytyy olla suurempia kuin nolla", True)
        else:
            iku.tyhjaa_kentan_sisalto(elementit["leveys"])
            iku.tyhjaa_kentan_sisalto(elementit["korkeus"])
            peli_aloita()
            iku.lopeta()
    except ValueError:
        iku.avaa_viesti_ikkuna("Virhe", "Arvojen täytyy olla kokonaislukuja", True)


def yllata():
    '''Arpoo pelin kentän koon'''
    peli['korkeus'] = ran.randint(10, 30)
    peli['leveys'] = ran.randint(10, 30)
    peli_aloita()
    iku.lopeta()


def tulokset():
    '''Funktio hakee tulokset tallennetusta tiedostosta sekä näyttää 
    ne pelaajalle'''
    pass


def lopeta():
    '''Funktio sulkee ohjelman'''
    iku.lopeta()


def mainmenu():
    '''Valikon mainfunktio joka luo käyttöikkunan käyttäen ikkunastoa'''
    ikkuna = iku.luo_ikkuna('Miinaharava')
    kehys1 = iku.luo_kehys(ikkuna)
    elementit["kehys1"] = iku.luo_kehys(ikkuna, iku.YLA)
    elementit["kehys2"] = iku.luo_kehys(ikkuna, iku.ALA)
    iku.luo_nappi(kehys1, "Aloita peli", aloita_peli)
    iku.luo_nappi(kehys1, "Katsele tuloksia", tulokset)
    iku.luo_nappi(kehys1, "Lopeta", lopeta)
    elementit["teksti1"] = iku.luo_tekstilaatikko(elementit["kehys1"], 20, 3)
    elementit["teksti2"] = iku.luo_tekstilaatikko(elementit["kehys2"], 20, 1)
    iku.kirjoita_tekstilaatikkoon(elementit["teksti1"], "MIINAHARAVA")
    iku.kirjoita_tekstilaatikkoon(elementit["teksti2"], "A game by Aleksi")
    iku.kaynnista()


def peli_aloita():
    '''Funktio joka hoitaa miinaharava pelin aloitusjärjestelyn'''
    ikkuna = iku.luo_ikkuna('Ladataan')
    iku.kaynnista()
    luo_kentta(peli["korkeus"], peli["leveys"])
    miinoita(kentta["alue"], peli["jaljella"])
    mainpeli()
    


def mainpeli():
    '''Itse miinaharavan main funktio'''
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(peli["leveys"]*40, peli["korkeus"]*40)
    hav.aseta_hiiri_kasittelija(kasittele_hiiri)
    hav.aseta_toistuva_kasittelija #TÄNNE JÄÄTIIN KESKEN


def luo_kentta(korkeus, leveys):
    '''Funktio joka luo globaalin listan joka toimii pelikenttänä
    sekä luo listan koordinaateista jotka ovat kentällä'''
    miinakentta = []
    for rivi in range(korkeus):
        miinakentta.append([])
        for sarake in range(leveys):
            miinakentta[-1].append(' ')
    kentta["alue"] = miinakentta
    for x in range(leveys):
        for y in range(korkeus):
            peli["jaljella"].append((x, y))


def kasittele_hiiri(x, y, painike, muokkausnäppäimet):
    if painike == 1:
        if kentta[y][x] == 'x':
            havio()
        elif kentta[y][x] == ' ':
            tulva(kentta["alue"], x, y)
    elif painike == 4:
        merkkaa()


def miinoita(alue, vapaa):
    '''Funktio joka arpoo miinojen määrän sekä miinoittaa pelikentän'''
    pelialue = peli["leveys"] * peli["korkeus"]
    miina_ala = int(pelialue / ran.randint(3, 5))
    miina_yla = int(pelialue / ran.randint(2, 3))
    peli["miinat"] = ran.randint(miina_ala, miina_yla)
    for i in range(peli["miinat"]):
        krd = ran.choice(vapaa)
        alue[krd[1]][krd[0]] = 'x'
        vapaa.remove(krd)


def piirra_kentta():
    '''Funktio joka piirtää pelikentän peli-ikkunaan.
    Funktiota kutsutaan aina kun pelimoottori pyytää ruudun päivitystä.'''
    pass


def havio():
    '''Funktio joka käsittelee pelaajan häviön.'''
    pass


def tulva(lista, x, y):
    '''Funktio joka avaa pelaajalle ruutuja. Ruutuja jotka ovat'''
    naatit = [(x, y)]
    y_raja = len(lista)
    x_raja = len(lista[0])
    naatit2 = [(x, y)]
    if lista[y][x] == 'x':
        pass
    else:
        while naatit != []:
            x_krd, y_krd = naatit.pop(-1)
            lista[y_krd][x_krd] = 'y'
            vali_aika = []
            m = 0
            r = 0
            for i in range(y_krd-1, y_krd+2, 2):
                if i < 0 or i >= y_raja:
                    r += 1
                elif lista[i][x_krd] == ' ':
                    vali_aika.append((x_krd, i))
                elif lista[i][x_krd] == 'x':
                    m += 1
            for a in range(x_krd-1, x_krd+2, 2):
                if a < 0 or a >= x_raja:
                    r +=1
                elif lista[y_krd][a] == ' ':
                    vali_aika.append((a, y_krd))
                elif lista[y_krd][a] == 'x':
                    m += 1
            if len(vali_aika) > 1:
                naatit.extend(vali_aika)
                naatit2.extend(vali_aika)
            if m >= 1 and r > 0:
                lista[y_krd][x_krd] = 'r'
        while naatit2 != []:
            x_krd, y_krd = naatit2.pop(-1)
            n = 0
            t = 0
            for i in range(y_krd-1, y_krd+2):
                if i < 0 or i >= y_raja:
                    continue
                for a in range(x_krd-1, x_krd+2):
                    if a < 0 or a >= x_raja or (i, a) == (y_krd, x_krd):
                        continue
                    elif lista[i][a] == 'x':
                        n += 1
            if (x_krd, y_krd) == (x, y) or lista[y_krd][x_krd] != 'r':
                lista[y_krd][x_krd] = str(n)
            elif lista[y_krd][x_krd] == 'r':
                lista[y_krd][x_krd] = ' '


def merkkaa():
    '''Funktio joka merkkaa pisteen miinaksi'''
    pass

if __name__ == "__main__":
    peli_aloita()