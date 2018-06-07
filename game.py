# zignoruj te linijke
from lib import *


wysokosc = 500
szerokosc = 500
okno = stworz_okno_gry(szerokosc, wysokosc)
szerokosc_paletki = 10
wysokosc_paletki = 60

pilka = stworz_pilke()
pilka.ustaw_rozmiary(10, 10)
pilka.przesun_do(szerokosc / 2, wysokosc / 2)
pilka.ustaw_predkosc(2.5)
pilka.zawsze_odbijaj_od_scian()
pilka.zawsze_odbijaj_od_paletek()


lewa_paletka = stworz_paletke()
lewa_paletka.ustaw_rozmiary(szerokosc_paletki, wysokosc_paletki)
lewa_paletka.przesun_do(20, (wysokosc - wysokosc_paletki) / 2)
lewa_paletka.zawsze_odbijaj_od_scian()

prawa_paletka = stworz_paletke()
prawa_paletka.ustaw_rozmiary(szerokosc_paletki, wysokosc_paletki)
prawa_paletka.przesun_do(szerokosc - 20 - szerokosc_paletki, (wysokosc - wysokosc_paletki) / 2)
prawa_paletka.zawsze_odbijaj_od_scian()

jesli(nacisniety_klawisz, gora).to(prawa_paletka.przesun_do_gory)
jesli(nacisniety_klawisz, dol).to(prawa_paletka.przesun_w_dol)
jesli(nacisniety_klawisz, w).to(lewa_paletka.przesun_do_gory)
jesli(nacisniety_klawisz, s).to(lewa_paletka.przesun_w_dol)

jesli(pilka.dotyka_prawej_sciany).to(lewa_paletka.zwieksz_punkty)
jesli(pilka.dotyka_prawej_sciany).to(rozpocznij_nowa_runde)

jesli(pilka.dotyka_lewej_sciany).to(prawa_paletka.zwieksz_punkty)
jesli(pilka.dotyka_lewej_sciany).to(rozpocznij_nowa_runde)



def w_kazdej_klatce():
	pilka.aktualizuj_stan()
	pilka.rysuj(okno)

	lewa_paletka.rysuj(okno)
	lewa_paletka.aktualizuj_stan()

	prawa_paletka.rysuj(okno)
	prawa_paletka.aktualizuj_stan()

	wyswietl_tekst(okno, lewa_paletka.punkty, 30, 30)
	wyswietl_tekst(okno, prawa_paletka.punkty, szerokosc - 50, 30)
