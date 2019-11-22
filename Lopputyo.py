'''Moduuli luo päävalikon pelille, päävalikkoon sisältyy pelin
aloittaminen jossa pelaaja voi säätää haluamansa dimensiot että miinojen
määrä, katsella tilastoja, että sulkea ohjelman'''

import haravasto as hav
import ikkunasto as iku

elementit = {
    "kehys": None,
    "teksti": None,
    "input": None,
    "peli": None
}

koordinaatit = {
    "leveys": None,
    "korkeus": None
}

def aloita_peli():
    '''Funktio kysyy pelaajalta kentän koon sekä miinojen määrän sekä
    palauttaa nämä arvot'''
    elementit["peli"] = iku.luo_ali_ikkuna('')
    elementit["teksti"] = iku.luo_tekstilaatikko(elementit["peli"], 25, 5)
    elementit["input"] = iku.luo_tekstikentta(elementit["peli"])
    iku.luo_nappi(elementit["peli"], 'Syötä arvo', arvo_kasittelija)
    iku.kirjoita_tekstilaatikkoon(elementit["teksti"], "Syötä alueen korkeus", True)
    

def arvo_kasittelija():
    '''Funktio hakee ja tarkistaa pelaajan antaman arvon'''
    try:
        krd = int(iku.lue_kentan_sisalto(elementit["input"]))
        iku.tyhjaa_kentan_sisalto(elementit["input"])
        if krd <= 0:
            iku.kirjoita_tekstilaatikkoon(elementit["teksti"], "Arvon täytyy olla suurempi kuin nolla", True)
        else:
            return krd    
    except ValueError:
        iku.kirjoita_tekstilaatikkoon(elementit["teksti"], "Arvon täytyy olla kokonaisluku", True)

  

def tulokset():
    '''Funktio hakee tulokset tallennetusta tiedostosta sekä näyttää 
    ne pelaajalle'''
    pass

def lopeta():
    '''Funktio sulkee ohjelman'''
    iku.lopeta()

def main():
    '''Luo käyttöikkunan käyttäen ikkunastoa'''
    ikkuna = iku.luo_ikkuna('Miinaharava')
    kehys1 = iku.luo_kehys(ikkuna)
    elementit["kehys"] = iku.luo_kehys(ikkuna)
    iku.luo_nappi(kehys1, "Aloita peli", aloita_peli)
    iku.luo_nappi(kehys1, "Katsele tuloksia", tulokset)
    iku.luo_nappi(kehys1, "Lopeta", lopeta)
    elementit["teksti"] = iku.luo_tekstilaatikko(elementit["kehys"], 30, 10)
    iku.kaynnista()



if __name__ == "__main__":
    main()