import haravasto as hav


def piirra_kentta():
    """
Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
ruudun näkymän päivitystä.
"""
    hav.tyhjaa_ikkuna()
    hav.piirra_tausta()
    hav.aloita_ruutujen_piirto()
    for y_krd, ruutu_y in enumerate(planeetta):
        print(y_krd, ruutu_y)
        isoy = y_krd * 40
        for x_krd, ruutu_x in enumerate(ruutu_y):
                isox = x_krd * 40
                hav.lisaa_piirrettava_ruutu(ruutu_x, isox, isoy)
    hav.piirra_ruudut()


def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(600, 400)
    hav.aseta_piirto_kasittelija(piirra_kentta)
    hav.aloita()


def tulva6(lista, x, y):
    naatit = [(x, y)]
    y_raja = len(lista)
    x_raja = len(lista[0])
    if lista[y][x] == 'x':
        pass
    else:
        n = 0
        for i in range(y-1, y+2):
            if i < 0 or i >= y_raja:
                continue
            for a in range(x-1, x+2):
                if a < 0 or a >= x_raja or (i, a) == (y, x):
                        continue
                elif lista[i][a] == 'x':
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
                        elif lista[i][a] == 'x':
                            r += 1
                            n += 1
                        elif lista[i][a] != ' ':
                            continue
                        vali_aika.append((a, i))
                if r == 0:
                    naatit.extend(vali_aika)
                lista[y_krd][x_krd] = str(n)
                print(lista)
                




planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
    [" ", "x", "x", "x", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
    ["x", "x", "x", "x", "x", "x", "x", "x", " ", "x", " ", " ", " "], 
    ["x", "x", "x", "x", " ", " ", " ", " ", " ", " ", "x", " ", " "], 
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]


tulva6(planeetta, 5, 0)
main()