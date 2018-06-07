import pygame
import random
import math


pygame.init()
pygame.font.init()

# zmienne lokalne
fps = 60
paletki = []
obiekty = []
czcionka = pygame.font.SysFont("arial", 20)
instrukcje_warunkowe = []

# klawisze
gora = pygame.K_UP
dol = pygame.K_DOWN
w = pygame.K_w
s = pygame.K_s

# kolory
bialy = (255, 255, 255)
czarny = (0, 0, 0)
czerwony = (255, 0, 0)
niebieski = (0, 0, 255)


class InstrukcjaWarunkowa(object):
    def __init__(self):
        self.warunek = None
        self.instrukcja = None
        self.argumenty_warunku = []
        self.argumenty_instrukcji = []

    def ustaw_warunek(self, warunek, *argumenty):
        if callable(warunek):
            self.warunek = warunek
            self.argumenty_warunku = argumenty
        else:
            print("Niepoprawny warunek.")

        return self

    def to(self, instrukcja, *argumenty):
        if callable(instrukcja):
            self.instrukcja = instrukcja
            self.argumenty_instrukcji = argumenty

            if hasattr(instrukcja, "__self__"):
                instrukcja.__self__.instrukcje_warunkowe.append(self)
            else:
                instrukcje_warunkowe.append(self)
        else:
            print("Niepoprawna instrukcja.")

    def sprobuj_wykonac(self):
        if (self.warunek
           and self.warunek(*self.argumenty_warunku)
           and self.instrukcja):
            self.instrukcja(*self.argumenty_instrukcji)


def jesli(warunek, *argumenty):
    return InstrukcjaWarunkowa().ustaw_warunek(warunek, *argumenty)


class nie(object):
    def __init__(self, instrukcja, *argumenty):
        self.instrukcja = instrukcja
        self.argumenty = argumenty

    def __call__(self):
        return not self.instrukcja(*self.argumenty)


class Punkt(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class ObiektGry(object):
    def __init__(self):
        obiekty.append(self)
        self.x = 0
        self.y = 0
        self.poczatkowy_x = 0
        self.poczatkowy_y = 0
        self.szerokosc = 0
        self.wysokosc = 0
        self.kolor = bialy
        self.instrukcje_warunkowe = []

    def ustaw_rozmiary(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def przesun_do(self, x, y):
        self.x = x
        self.y = y
        self.poczatkowy_x = x
        self.poczatkowy_y = y

    def aktualizuj_stan(self):
        for instrukcja in self.instrukcje_warunkowe:
            instrukcja.sprobuj_wykonac()

    def resetuj(self):
        self.x = self.poczatkowy_x
        self.y = self.poczatkowy_y

    def ustaw_kolor(self, kolor):
        self.kolor = kolor


class Paletka(ObiektGry):
    def __init__(self):
        super(Paletka, self).__init__()
        self.punkty = 0
        self.odbijalna_od_scian = False

    def zawsze_odbijaj_od_scian(self):
        self.odbijalna_od_scian = True

    def zwieksz_punkty(self):
        self.punkty += 1

    def przesun_do_gory(self):
        self.y -= 4

    def przesun_w_dol(self):
        self.y += 4

    def aktualizuj_stan(self):
        super(Paletka, self).aktualizuj_stan()

        if self.odbijalna_od_scian:
            szerokosc, wysokosc = pygame.display.get_surface().get_size()
            if self.y < 0:
                self.y = 0

            if self.y + self.wysokosc > wysokosc:
                self.y = wysokosc - self.wysokosc

    def rysuj(self, okno):
        pygame.draw.rect(
            okno, self.kolor, (self.x, self.y, self.szerokosc, self.wysokosc))


class Pilka(ObiektGry):
    def __init__(self):
        super(Pilka, self).__init__()
        self.promien = self.szerokosc / 2
        self.predkosc = Punkt()
        self.odbijalna_od_paletek = False
        self.odbijalna_od_scian = False
        self.dotyka_lewej = False
        self.dotyka_prawej = False

    def ustaw_rozmiary(self, szerokosc, wysokosc):
        super(Pilka, self).ustaw_rozmiary(szerokosc, wysokosc)
        self.promien = int(self.szerokosc / 2)

    def ustaw_predkosc(self, predkosc):
        kat = random.uniform(0, 2 * math.pi)
        self.predkosc.x = math.sin(kat) * predkosc
        self.predkosc.y = math.cos(kat) * predkosc

    def zawsze_odbijaj_od_paletek(self):
        self.odbijalna_od_paletek = True

    def zawsze_odbijaj_od_scian(self):
        self.odbijalna_od_scian = True

    def odbij_od(self, obiekt):
        near = Punkt()
        far = Punkt()
        entry = Punkt()
        exit = Punkt()
        normal = Punkt()
        inf = float("inf")
        velocity = self.predkosc

        if velocity.x > 0:
            near.x = obiekt.x - (self.x + self.szerokosc)
            far.x = (obiekt.x + obiekt.szerokosc) - self.x
        else:
            near.x = (obiekt.x + obiekt.szerokosc) - self.x
            far.x = obiekt.x - (self.x + self.szerokosc)

        if velocity.y > 0:
            near.y = obiekt.y - (self.y + self.wysokosc)
            far.y = (obiekt.y + obiekt.wysokosc) - self.y
        else:
            near.y = (obiekt.y + obiekt.wysokosc) - self.y
            far.y = obiekt.y - (self.y + self.wysokosc)

        if velocity.x == 0:
            entry.x = -inf
            exit.x = inf
        else:
            entry.x = near.x / velocity.x
            exit.x = far.x / velocity.x
        if velocity.y == 0:
            entry.y = -inf
            exit.y = inf
        else:
            entry.y = near.y / velocity.y
            exit.y = far.y / velocity.y

        entry_time = max(entry.x, entry.y)
        exit_time = min(exit.x, exit.y)

        if (entry_time > exit_time
           or entry.x < 0 and entry.y < 0
           or entry.x > 1
           or entry.y > 1):
            return

        if entry.x > entry.y:
            if near.x < 0:
                normal.x = 1
                normal.y = 0
            else:
                normal.x = -1
                normal.y = 0
        else:
            if near.y < 0:
                normal.x = 0
                normal.y = 1
            else:
                normal.x = 0
                normal.y = -1

        if bool(normal.x):
            self.predkosc.x *= -1
            self.losuj_predkosc()
        elif bool(normal.y):
            self.predkosc.y *= -1
            self.losuj_predkosc()

    def losuj_predkosc(self):
        kat = math.atan2(self.predkosc.x, self.predkosc.y)
        dlugosc = math.sqrt(self.predkosc.x ** 2 + self.predkosc.y ** 2)
        rnd = random.uniform(-0.3, 0.3)
        kat += rnd
        self.predkosc.x = math.sin(kat) * dlugosc
        self.predkosc.y = math.cos(kat) * dlugosc

    def odbij_od_scian(self):
        wysokosc, szerokosc = pygame.display.get_surface().get_size()

        if self.x + self.predkosc.x < 0:
            self.dotyka_lewej = True
            self.predkosc.x *= -1
            self.losuj_predkosc()
        else:
            self.dotyka_lewej = False

        if self.x + self.predkosc.x + self.szerokosc > szerokosc:
            self.dotyka_prawej = True
            self.predkosc.x *= -1
            self.losuj_predkosc()
        else:
            self.dotyka_prawej = False

        if (self.y + self.predkosc.y < 0
           or self.y + self.predkosc.y + self.wysokosc > wysokosc):
            self.predkosc.y *= -1
            self.losuj_predkosc()

    def dotyka_prawej_sciany(self):
        return self.dotyka_prawej

    def dotyka_lewej_sciany(self):
        return self.dotyka_lewej

    def aktualizuj_stan(self):
        if self.odbijalna_od_scian:
            self.odbij_od_scian()

        if self.odbijalna_od_paletek:
            for paletka in paletki:
                self.odbij_od(paletka)

        super(Pilka, self).aktualizuj_stan()

        self.x += self.predkosc.x
        self.y += self.predkosc.y

    def rysuj(self, okno):
        pygame.draw.circle(
            okno, self.kolor,
            (int(self.x) + self.promien, int(self.y) + self.promien),
            self.promien)


def stworz_paletke():
    paletki.append(Paletka())
    return paletki[-1]


def stworz_pilke():
    return Pilka()


def stworz_okno_gry(szerokosc, wysokosc):
    okno = pygame.display.set_mode((wysokosc, szerokosc))
    pygame.display.set_caption("okno gry")

    return okno


def nacisniety_klawisz(klawisz):
    return pygame.key.get_pressed()[klawisz]


def rozpocznij_nowa_runde():
    for obiekt in obiekty:
        obiekt.resetuj()


def wyswietl_tekst(okno, tekst, x, y):
    powierzchnia = czcionka.render(str(tekst), False, bialy)
    okno.blit(powierzchnia, (x, y))
