import haravasto

ARVOT = {
    1: 'vasen',
    4: 'oikea',
    2: 'keski'
}

def kasittele_hiiri(x, y, painike, muokkausnäppäimet):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    print('Hiiren nappia {} painettiin kohdassa {}, {}'.format(ARVOT[painike], x, y))

def main():
    """
    Luo sovellusikkunan ja asettaa käsittelijäfunktion hiiren klikkauksille.
    Käynnistää sovelluksen.
    """
    haravasto.luo_ikkuna()
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()

if __name__ == "__main__":
    main()