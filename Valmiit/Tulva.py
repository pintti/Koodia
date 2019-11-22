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
        isoy = y_krd * 40
        for x_krd, ruutu_x in enumerate(ruutu_y):
                isox = x_krd * 40
                if planeetta[y_krd][x_krd] == "x":
                    hav.lisaa_piirrettava_ruutu("x", isox, isoy)
                elif planeetta[y_krd][x_krd] == '0':
                    hav.lisaa_piirrettava_ruutu("0", isox, isoy)
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


def tulvataytto(lista, x, y):
    naatit = [(x, y)]
    y_raja = len(lista)-1
    x_raja = len(lista[0])-1
    if lista[y][x] == 'x':
        pass
    else:
        while naatit != []:
            x_krd, y_krd = naatit.pop(-1)
            lista[y_krd][x_krd] = '0'
            for i in range(y_krd-1, y_krd+2):
                if i < 0:
                    continue
                elif i > y_raja:
                    break
                for a in range(x_krd-1, x_krd+2):
                    if a < 0:
                        continue
                    elif a > x_raja:
                        break
                    if lista[i][a] == 'x':
                        continue
                    elif lista[i][a] == ' ':
                        naatit.append((a, i))


planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]

tulvataytto(planeetta, 1, 1)
main()