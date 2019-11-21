import haravasto as hav
import random

tila = {
    "kentta": []
}

def miinoita(alue, vapaa, miinat):
    """
Asettaa kentällä N kpl miinoja satunnaisiin paikkoihin.
"""
    for i in range(miinat):
        krd = random.choice(vapaa)
        alue[krd[1]][krd[0]] = "x"
        vapaa.remove(krd)



def piirra_kentta():
    """
Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
ruudun näkymän päivitystä.
"""
    hav.tyhjaa_ikkuna()
    hav.piirra_tausta()
    hav.aloita_ruutujen_piirto()
    for y_krd, ruutu_y in enumerate(tila["kentta"]):
        isoy = y_krd * 40
        for x_krd, ruutu_x in enumerate(ruutu_y):
                isox = x_krd * 40
                if tila["kentta"][y_krd][x_krd] == "x":
                    hav.lisaa_piirrettava_ruutu("x", isox, isoy)
                else:
                    hav.lisaa_piirrettava_ruutu(" ", isox, isoy)
    hav.piirra_ruudut()
    

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(600, 400)
    hav.aseta_piirto_kasittelija(piirra_kentta)
    hav.aloita()

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

    miinoita(tila["kentta"], jaljella, 35)
    main()