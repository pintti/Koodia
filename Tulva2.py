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
                    hav.lisaa_piirrettava_ruutu(" ", isox, isoy)
                elif planeetta[y_krd][x_krd] == ' ':
                    hav.lisaa_piirrettava_ruutu(" ", isox, isoy)
                else:
                    hav.lisaa_piirrettava_ruutu(planeetta[y_krd][x_krd], isox, isoy)
    hav.piirra_ruudut()


def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    hav.lataa_kuvat("spritet")
    hav.luo_ikkuna(600, 400)
    hav.aseta_piirto_kasittelija(piirra_kentta)
    hav.aloita()


def tulva3(lista, x, y):
    naatit = [(x, y)]
    y_raja = len(lista)-1
    x_raja = len(lista[0])-1
    if lista[y][x] == 'x':
        pass
    else:
        while naatit != []:
            x_krd, y_krd = naatit.pop(-1)
            n = 0
            m = 0
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
                    if (i, a) == (y_krd, x_krd):
                        continue
                    elif lista[i][a] == 'x':
                        n += 1
                        m += 1
                    elif lista[i][a] != ' ':
                        m +=1
            lista[y_krd][x_krd] = str(n)
            for i in range(y_krd-1, y_krd+2, 2):
                if i < 0 or i > y_raja:
                    continue
                elif lista[i][x_krd] == ' ':
                    naatit.append((x_krd, i))
            for a in range(x_krd-1, x_krd+2, 2):
                if a < 0 or a > x_raja:
                    continue
                elif lista[y_krd][a] == ' ':
                    naatit.append((a, y_krd))
            
def tulva4(lista, x, y):
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




planeetta = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]

planeetta2 = [
    [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
    [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", " ", " "], 
    [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
    ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
    ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
    [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
]


tulva4(planeetta, 6, 0)
main()
