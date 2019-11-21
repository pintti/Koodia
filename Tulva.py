

def miinoita(alue, vapaa, miinat):
    """
Asettaa kentällä N kpl miinoja satunnaisiin paikkoihin.
"""
    for i in range(miinat):
        krd = random.choice(vapaa)
        alue[krd[1]][krd[0]] = "x"
        vapaa.remove(krd)

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(600, 400)
    hav.aseta_piirto_kasittelija(piirra_kentta)
    hav.aloita()

def tulvataytto(lista, x, y):
    if lista[y][x] == 'x':
        pass
    else:
        pass