import haravasto as hav
import random

tila = {
    "kentta": []
}

def miinoita(kentta, vapaa, miinat):
    """
Asettaa kentällä N kpl miinoja satunnaisiin paikkoihin.
"""
    x, y = random.choice(vapaa)

def piirra_kentta():
    """
Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
ruudun näkymän päivitystä.
"""
    hav.tyhjaa_ikkuna()
    hav.aloita_ruutujen_piirto()

    

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(600, 400)
    hav.aseta_piirto_kasittelija(piirra_kentta)

if __name__ == "__main__":
    kentta = []
    for rivi in range(10):
        kentta.append([])
        for sarake in range(15):
            kentta[-1].append(" ")

    tila["kentta"] = kentta

    jaljella = []
    for x in range(15):
        for y in range(10):
            jaljella.append((x, y))

    main()