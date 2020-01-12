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

elementit = {
    "kehys1": None,
    "teksti1": None,
    "kehys2": None,
    "teksti2": None,
    "korkeus": None,
    "leveys": None,
    "miinat": None,
    'vika1': None,
    'vikaik': None
}

peli = {
    "leveys": 0,
    "korkeus": 0,
    "miinat": 0,
    "miinakrd": [],
    "liputetut": 0,
    "jaljella": [],
    "start": 0
}

kentta = {
    "alue": [],
    "tarkistus": []
}

stats = {
    'nimi': None,
    'liputetut': 0,
    'aika': 0
}

data ={
    'tilasto': []
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
            liput["peli"] = True
            iku.lopeta()
    except ValueError:
        iku.avaa_viesti_ikkuna("Virhe", "Arvojen täytyy olla kokonaislukuja", True)


def yllata():
    '''Arpoo pelin kentän koon'''
    peli['korkeus'] = ran.randint(10, 20)
    peli['leveys'] = ran.randint(10, 20)
    pelialue = peli["leveys"] * peli["korkeus"]
    miina_ala = int(pelialue / ran.randint(4, 5))
    miina_yla = int(pelialue / ran.randint(3, 4))
    peli["miinat"] = ran.randint(miina_ala, miina_yla)
    liput["peli"] = True
    iku.lopeta()


def tulokset():
    '''Funktio hakee tulokset tallennetusta tiedostosta sekä näyttää 
    ne pelaajalle'''
    with open('tulokset.txt') as file:
        data = json.load(file)
        piste = iku.luo_ali_ikkuna('Tilastot')
        print(data)
        for p in data['tilasto']:
            print(p)
            iku.luo_tekstirivi(piste, 'Nimi: {}, Liputetut: {}, Aika: {}'.format(p['nimi'], p['liputetut'], p['aika']))


def lopeta():
    '''Funktio sulkee ohjelman'''
    liput["jatka"] = False
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
    peli['miinakrd'] = []
    liput["peli"] = False
    liput['voitto'] = 0
    peli["liputetut"] = 0
    liput['save'] = False
    peli['jaljella'] = []
    luo_kentta(peli["korkeus"], peli["leveys"])
    miinoita(kentta["alue"], peli["jaljella"])
    kentta["tarkistus"] = copy.deepcopy(kentta["alue"])
    


def mainpeli():
    '''Itse miinaharavan main funktio'''
    peli["start"] = time.time()
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(peli["leveys"]*40, peli["korkeus"]*40)
    hav.aseta_piirto_kasittelija(piirra_kentta)
    hav.aseta_hiiri_kasittelija(kasittele_hiiri)
    hav.aseta_toistuva_kasittelija(toistuva_kasittelija, 1/4)
    hav.aloita()


def luo_kentta(korkeus, leveys):
    '''Funktio joka luo globaalin listan joka toimii pelikenttänä
    sekä luo listan koordinaateista jotka ovat kentällä'''
    miinakentta = []
    for rivi in range(korkeus):
        miinakentta.append([])
        for sarake in range(leveys):
            miinakentta[-1].append(' ')
    kentta["alue"] = copy.deepcopy(miinakentta)
    for x in range(leveys):
        for y in range(korkeus):
            peli["jaljella"].append((x, y))


def kasittele_hiiri(x, y, painike, muokkausnäppäimet):
    '''Funktio käsittelee hiiren :)'''
    if liput['voitto'] == 0:
        if painike == 1:
            tulva(kentta["alue"], int(x/40), int(y/40))
        elif painike == 4:
            merkkaa(kentta["alue"], int(x/40), int(y/40))


def miinoita(alue, vapaa):
    '''Funktio joka arpoo miinojen määrän sekä miinoittaa pelikentän'''
    for i in range(peli["miinat"]):
        krd = ran.choice(vapaa)
        alue[krd[1]][krd[0]] = 'x'
        peli["miinakrd"].append(krd)
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
            elif ruutu_x == 'h':
                hav.lisaa_piirrettava_ruutu('x', isox, isoy)
            else:
                hav.lisaa_piirrettava_ruutu(ruutu_x, isox, isoy)
    hav.piirra_ruudut()


def havio(lista):
    '''Funktio joka käsittelee pelaajan häviön. Häviö näyttää kaikkien miinojen
    paikat ja kertoo pelaajalle häviöstä sekä antaa tallentaa pelaajan tilan'''
    for x, y in peli['miinakrd']:
        lista[y][x] = 'h'
    liput['voitto'] = 2
    stats['aika'] = round(time.time() - peli['start'], 1)
    stats['liputetut'] = peli['liputetut']
    

def voitto():
    '''Funktio joka suorittaa pelaajalle voiton'''
    liput['voitto'] = 1
    stats['aika'] = round(time.time() - peli['start'], 1)
    stats['liputetut'] = peli['liputetut']


def tulva(lista, x, y):
    '''Funktio joka avaa pelaajalle ruutuja. Ruudut jotka ovat miinojen
    vieressä numeroidaan vastaavasti. Mikäli jos ruutu jota avataan on 
    miinan vieressä avataan vain tämä ruutu. Tulva pysähtyy ensimmäisiin
    numeroituihin ruutuihin.'''
    naatit = [(x, y)]
    y_raja = len(lista)
    x_raja = len(lista[0])
    if kentta["tarkistus"][y][x] == 'x':
        havio(lista)
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
            if (x, y) in peli['jaljella']:
                peli['jaljella'].remove((x, y))
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
                if (x_krd, y_krd) in peli['jaljella']:
                    peli['jaljella'].remove((x_krd, y_krd))


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


def toistuva_kasittelija(aika):
    '''Toistuva käsittelijä joka tarkistaa voittaako pelaaja pelin'''
    if peli["liputetut"] == peli["miinat"] and peli['jaljella'] == []:
        voitto()
        peli_loppu()
    elif liput['voitto'] == 2:
        peli_loppu()
        pass
        

def peli_loppu():
    '''Funktio joka suorittaa kaiken pelin loppumisen jälkeen tapahtuvan'''
    ikkuna = iku.luo_ikkuna('')
    ali = iku.luo_kehys(ikkuna)
    if liput['voitto'] == 1:
        iku.avaa_viesti_ikkuna('', 'VOITIT PELIN')
    elif liput['voitto'] == 2:
        iku.avaa_viesti_ikkuna('', 'HÄVISIT PELIN')
    iku.luo_tekstirivi(ali, 'Liputit {} miinaa, kun miinoja oli {} kpl'.format(peli['liputetut'], peli['miinat']))
    iku.luo_tekstirivi(ali, 'Aikaa kului {} sekuntia'.format(stats['aika']))
    iku.luo_nappi(ali, 'Pelaa uudelleen', uusiksi)
    iku.luo_nappi(ali, 'Tallenna tulokset', save)
    iku.luo_nappi(ali, 'Palaa päävalikkoon', back)
    iku.kaynnista()


def uusiksi():
    '''Restart nappi periaatteessa'''
    liput['peli'] = True
    iku.lopeta()
    hav.lopeta()


def back():
    '''Mainmenuun vievä funktio'''
    hav.lopeta()
    iku.lopeta()


def main():
    '''Päälooppi joka pyörittää peliä'''
    while liput["jatka"]:
        mainmenu()
        while liput["peli"]:
            peli_aloita()
            mainpeli()
            if liput['save']:
                tallenna()


def save():
    '''Funktio kysyy pelaajan nimen ja tallentaa tämän ajan 
    että liputetut miinat'''
    elementit['vikaik'] = iku.luo_ali_ikkuna('')
    iku.luo_tekstirivi(elementit['vikaik'], 'Kirjoita nimesi')
    elementit['vika'] = iku.luo_tekstikentta(elementit['vikaik'])
    iku.luo_nappi(elementit['vikaik'], 'Syötä', nimi)


def nimi():
    '''Tallentaa sen nimen'''
    stats['nimi'] = iku.lue_kentan_sisalto(elementit['vika'])
    iku.tyhjaa_kentan_sisalto(elementit['vika'])
    iku.piilota_ali_ikkuna(elementit['vikaik'])
    ali = iku.luo_ali_ikkuna('')
    liput['save'] = True
    iku.luo_tekstirivi(ali, 'Tulokset tallennettu!')


def tallenna():
    '''Tulosten tallentamisen hoitava funktio'''
    try:
        with open('tulokset.txt', 'r') as file:
            data = json.load(file)
        data['tilasto'].append(stats)
        print(data['tilasto'])
        with open('tulokset.txt', 'w') as file:
            json.dump(data, file)
    except json.JSONDecodeError:
        with open('tulokset.txt', 'w') as file:
            data['tilasto'].append(stats)
            json.dump(data, file)


if __name__ == "__main__":
    main()
    