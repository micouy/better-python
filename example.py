# zmienne
wysokosc, szerokosc = 400, 400
szerokosc_paletki = 10
wysokosc_paletki = 60

okno = stworz_okno_gry(wysokosc, szerokosc)
lewa_paletka = stworz_paletke()
prawa_paletka = stworz_paletke()
pilka = stworz_pilke()

# instrukcje
lewa_paletka.ustaw_rozmiary(szerokosc_paletki, wysokosc_paletki)
lewa_paletka.ustaw_kolor(niebieski)
lewa_paletka.przesun_do(50, (wysokosc - wysokosc_paletki) / 2)
lewa_paletka.zawsze_odbijaj_od_scian()

jesli(nacisniety_klawisz, w).to(lewa_paletka.przesun_do_gory)
jesli(nacisniety_klawisz, s).to(lewa_paletka.przesun_w_dol)

prawa_paletka.ustaw_rozmiary(szerokosc_paletki, wysokosc_paletki)
prawa_paletka.ustaw_kolor(czerwony)
prawa_paletka.przesun_do(350 - szerokosc_paletki,
                         (wysokosc - wysokosc_paletki) / 2)
prawa_paletka.zawsze_odbijaj_od_scian()

jesli(nacisniety_klawisz, gora).to(prawa_paletka.przesun_do_gory)
jesli(nacisniety_klawisz, dol).to(prawa_paletka.przesun_w_dol)

pilka.ustaw_rozmiary(10, 10)
pilka.przesun_do(szerokosc / 2, wysokosc / 2)
pilka.ustaw_predkosc(2.5)
pilka.zawsze_odbijaj_od_scian()
pilka.zawsze_odbijaj_od_paletek()

jesli(pilka.dotyka_prawej_sciany).to(lewa_paletka.zwieksz_punkty)
jesli(pilka.dotyka_prawej_sciany).to(rozpocznij_nowa_runde)

jesli(pilka.dotyka_lewej_sciany).to(prawa_paletka.zwieksz_punkty)
jesli(pilka.dotyka_lewej_sciany).to(rozpocznij_nowa_runde)


# instrukcje powtarzane w kazdej klatce
def w_kazdej_klatce():
    lewa_paletka.aktualizuj_stan()
    prawa_paletka.aktualizuj_stan()
    pilka.aktualizuj_stan()

    lewa_paletka.rysuj(okno)
    prawa_paletka.rysuj(okno)
    pilka.rysuj(okno)

    wyswietl_tekst(okno, lewa_paletka.punkty, 20, 20)
    wyswietl_tekst(okno, prawa_paletka.punkty, szerokosc - 30, 20)
