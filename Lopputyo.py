'''Moduuli luo päävalikon pelille, päävalikkoon sisältyy pelin
aloittaminen jossa pelaaja voi säätää haluamansa dimensiot että miinojen
määrä, katsella tilastoja, että sulkea ohjelman'''

import haravasto as hav
import ikkunasto as iku
import random as ran
import time
import copy

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
    "leveys": None,
    "miinat": None
}

peli = {
    "leveys": 5,
    "korkeus": 5,
    "miinat": 10,
    "liputetut": 0,
    "jaljella": []
}

kentta = {
    "alue": [],
    "tarkistus": []
}

def aloita_peli():
    '''Funktio kysyy pelaajalta kentän koon sekä miinojen määrän sekä
    palauttaa nämä arvot. Avataan ali-ikkunaan jonne syötetään kentan
    leveys, korkeus sekä miinojen määrä (ei implementoitu vielä).'''
    ala = iku.luo_ali_ikkuna('')
    ala_kehys1 = iku.luo_kehys(ala)
    ala_kehys2 = iku.luo_kehys(ala)
    ala_teksti1 = iku.luo_tekstilaatikko(ala_kehys1, 20, 1)
    iku.kirjoita_tekstilaatikkoon(ala_teksti1, "Anna kentän korkeus")
    elementit["korkeus"] = iku.luo_tekstikentta(ala_kehys1)
    ala_teksti2 = iku.luo_tekstilaatikko(ala_kehys2, 20, 1)
    iku.kirjoita_tekstilaatikkoon(ala_teksti2, "Anna kentän leveys")
    elementit["leveys"] = iku.luo_tekstikentta(ala_kehys2)
    ala_kehys3 = iku.luo_kehys(ala)
    ala_teksti3 = iku.luo_tekstilaatikko(ala_kehys3, 20, 1)
    iku.kirjoita_tekstilaatikkoon(ala_teksti3, "Anna miinojen määrä")
    elementit["miinat"] = iku.luo_tekstikentta(ala_kehys3)
    iku.luo_nappi(ala_kehys2, 'Syötä arvot ja aloita peli', arvo_kasittelija)
    iku.luo_nappi(ala_kehys2, 'Yllätä minut', yllata)
    

def arvo_kasittelija():
    '''Funktio hakee ja tarkistaa pelaajan antaman arvon. Kentta on
    tekstikenttä johon käyttäjä kirjoittaa, teksti alue johon kirjoitetaan
    tekstiä.'''
    try:
        peli["korkeus"] = int(iku.lue_kentan_sisalto(elementit["korkeus"]))
        peli["leveys"] = int(iku.lue_kentan_sisalto(elementit["leveys"]))
        peli["miinat"] = int(iku.lue_kentan_sisalto(elementit["miinat"]))
        if peli["korkeus"] <= 0 or peli["leveys"] <= 0 or peli["miinat"] <= 0:
            iku.avaa_viesti_ikkuna("Virhe", "Arvojen täytyy olla suurempia kuin nolla", True)
        else:
            iku.tyhjaa_kentan_sisalto(elementit["leveys"])
            iku.tyhjaa_kentan_sisalto(elementit["korkeus"])
            iku.tyhjaa_kentan_sisalto(elementit["miinat"])
            peli_aloita()
            iku.lopeta()
    except ValueError:
        iku.avaa_viesti_ikkuna("Virhe", "Arvojen täytyy olla kokonaislukuja", True)


def yllata():
    '''Arpoo pelin kentän koon'''
    peli['korkeus'] = ran.randint(10, 21)
    peli['leveys'] = ran.randint(10, 21)
    pelialue = peli["leveys"] * peli["korkeus"]
    miina_ala = int(pelialue / ran.randint(4, 5))
    miina_yla = int(pelialue / ran.randint(3, 4))
    peli["miinat"] = ran.randint(miina_ala, miina_yla)
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
    luo_kentta(peli["korkeus"], peli["leveys"])
    miinoita(kentta["alue"], peli["jaljella"])
    kentta["tarkistus"] = copy.deepcopy(kentta["alue"])
    mainpeli()
    


def mainpeli():
    '''Itse miinaharavan main funktio'''
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(peli["leveys"]*40, peli["korkeus"]*40)
    hav.aseta_piirto_kasittelija(piirra_kentta)
    hav.aseta_hiiri_kasittelija(kasittele_hiiri)
    #hav.aseta_toistuva_kasittelija(toistuva_kasittelija) 
    #tämä pitää tehdä jossain vaiheessa
    hav.aloita()


def luo_kentta(korkeus, leveys):
    '''Funktio joka luo globaalin listan joka toimii pelikenttänä
    sekä luo listan koordinaateista jotka ovat kentällä'''
    miinakentta = []
    for rivi in range(korkeus):
        miinakentta.append([])
        for sarake in range(leveys):
            miinakentta[-1].append(' ')
    kentta["alue"] =copy.deepcopy(miinakentta)
    for x in range(leveys):
        for y in range(korkeus):
            peli["jaljella"].append((x, y))


def kasittele_hiiri(x, y, painike, muokkausnäppäimet):
    if painike == 1:
        tulva(kentta["alue"], int(x/40), int(y/40))
        piirra_kentta()
    elif painike == 4:
        merkkaa(kentta["alue"], int(x/40), int(y/40))
        piirra_kentta()
        tarkistavoitto()


def miinoita(alue, vapaa):
    '''Funktio joka arpoo miinojen määrän sekä miinoittaa pelikentän'''
    for i in range(peli["miinat"]):
        krd = ran.choice(vapaa)
        alue[krd[1]][krd[0]] = 'x'
        vapaa.remove(krd)


def piirra_kentta():
    '''Funktio joka piirtää pelikentän peli-ikkunaan.
    Funktiota kutsutaan aina kun pelimoottori pyytää ruudun päivitystä.'''
    hav.tyhjaa_ikkuna()
    hav.piirra_tausta()
    hav.aloita_ruutujen_piirto()
    for y_krd, ruutu_y in enumerate(kentta["alue"]):
        isoy = y_krd * 40
        for x_krd, ruutu_x in enumerate(ruutu_y):
            isox = x_krd * 40
            if ruutu_x == 'x':
                hav.lisaa_piirrettava_ruutu(' ', isox, isoy)
            else:
                hav.lisaa_piirrettava_ruutu(ruutu_x, isox, isoy)
    hav.piirra_ruudut()


def havio():
    '''Funktio joka käsittelee pelaajan häviön. Häviö näyttää kaikkien
    paikat ja kertoo pelaajalle häviöstä sekä antaa tallentaa pelaajan tilan'''
    pass


def tarkistavoitto():
    '''Funktio joka tarkistaa onko pelaaja voittanut'''
    pass

def tulva(lista, x, y):
    '''Funktio joka avaa pelaajalle ruutuja. Ruudut jotka ovat miinojen
    vieressä numeroidaan vastaavasti. Mikäli jos ruutu jota avataan on 
    miinan vieressä avataan vain tämä ruutu. Tulva pysähtyy ensimmäisiin
    numeroituihin ruutuihin.'''
    naatit = [(x, y)]
    y_raja = len(lista)
    x_raja = len(lista[0])
    print(lista[y][x])
    print(kentta["tarkistus"][y][x])
    if lista[y][x] == 'x':
        havio()
    elif lista[y][x] == 'f' and kentta["tarkistus"][y][x] == 'x':
        print('Hävisit')
    else:
        n = 0
        for i in range(y-1, y+2):
            if i < 0 or i >= y_raja:
                continue
            for a in range(x-1, x+2):
                if a < 0 or a >= x_raja or (i, a) == (y, x):
                        continue
                elif kentta["tarkistus"][i][a] == 'x':
                    n += 1
        if n >= 1:
            lista[y][x] = str(n)
        else:  
            while naatit != []:
                x_krd, y_krd = naatit.pop()
                vali_aika = []
                r = 0
                n = 0
                for i in range(y_krd-1, y_krd+2):
                    if i < 0 or i >= y_raja:
                        continue
                    for a in range(x_krd-1, x_krd+2):
                        if a < 0 or a >= x_raja or (i, a) == (y_krd, x_krd):
                            continue
                        elif kentta["tarkistus"][i][a] == 'x':
                            r += 1
                            n += 1
                        elif lista[i][a] != ' ':
                            continue
                        vali_aika.append((a, i))
                if r == 0:
                    naatit.extend(vali_aika)
                lista[y_krd][x_krd] = str(n)


def merkkaa(lista, x, y):
    '''Funktio joka merkkaa pisteen miinaksi'''
    if lista[y][x] == ' ' or lista[y][x] == 'x':
        if kentta["tarkistus"][y][x] == 'x':
            peli["liputetut"] += 1
            lista[y][x] = 'f'
        else:
            lista[y][x] = 'f'
    elif lista[y][x] == 'f':
        if kentta["tarkistus"][y][x] == 'x':
            peli["liputetut"] -= 1
            lista[y][x] = ' '
        else:
            lista[y][x] = ' '
        


    #if lista[y][x] == ' ':
    #    kentta["tarkistus"][y][x] = lista[y][x] 
    #    lista[y][x] = 'f'
    #elif kentta["tarkistus"][y][x] == 'x':
    #    lista[y][x] = 'f'
    #elif lista[y][x] == 'f':
    #    if kentta["tarkistus"][y][x] == 'x':
    #    lista[y][x] = kentta["tarkistus"][y][x]


def toistuva_kasittelija():
    pass

if __name__ == "__main__":
    mainmenu()