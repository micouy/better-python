# Jak czytać ściągę?
W tej ściądze wiele razy zobaczysz nawiasy `<...>`, takie jak te:

```python
<zmienna> = stworz_jakas_rzecz()
```

Użycie nawiasów `<...>` oznacza, że w tym miejscu ma się coś znajdować, (co dokładnie ma się znajdować zależy od nazwy między tymi nawiasami). W pokazanym przypadku należy wpisać nazwę zmiennej, w której będzie się znajdowała stworzona "rzecz". Zachowują się one tak samo, jak zmienne w matematyce. Nazwa zmiennej jest dowolna, jednak dobrze by było, żeby krótko opisywała, co przechowuje, na przykład:

```python
lewa_paletka = stworz_paletke()
```

W ściądze znajdują się również instrukcje korzystania z funkcji. Przykładem funkcji jest `stworz_paletke`. Funkcje to instrukcje składające się z *poleceń* oraz *nazwy*, a czasami również z *parametrów*. Jeżeli chcemy daną funkcję wykonać, czyli *wywołać*, musimy użyć nawiasów (tak samo, jak w matematyce).

```python
stworz_okno_gry(500, 500)
```

Funkcja `stworz_okno_gry` tworzy okno, w którym pojawi się gra. Wymaga ona podania dwóch parametrów - wysokości i szerokości okna. Wracając do nawiasów - w przypadku funkcji te nawiasy znajdują się w ściądze w miejscu, w którym mają znaleźć się właśnie parametry, na przykład:

```python
# dla wszystkich obiektów:
przesun_do(<x>, <y>)
```

Instrukcja `przesun_do` sprawia, że dany obiekt przesunie się do wybranych koordynatów - `x` i `y`. Jak pewnie zauważyłeś/aś, w kodzie pojawił się komentarz "dla wszystkich obiektów". Oznacza on, że instrukcja może być wywołana na każdym obiekcie. Co to znaczy? Najpierw musimy wprowadzić podział na instrukcje *ogólne* oraz *dla konkretnych obiektów*. Pierwsze są wywoływane jak w pierwszym przykładzie z funkcjami. Po prostu mamy nazwę funkcji, nawiasy oraz ewentualne parametry:

```python
stworz_okno_gry(500, 500)
```

Drugie mogą być wywoływane tylko na obiektach:

```python
pilka = stworz_pilke()
pilka.przesun_do(100, 200)

paletka = stworz_paletke()
paletka.przesun_do(50, 30)
```

Nie możemy przecież powiedzieć powietrzu, żeby przesunęło się w podane miejsce. Musi to być konkretny obiekt. Z tego samego powodu niektóre funkcje mogą być wywoływane tylko na określonym typie obiektu, na przykład piłce lub paletce:

```python
pilka = stworz_pilke()
pilka.ustaw_predkosc(2)
```

Prędkość może być ustawiona tylko piłce.


# Zmienne
Zmienne działają tak, jak w matematyce:

```python
x = 10
y = 5
z = x + y
```

Mogą przechowywać także obiekty tworzone za pomocą funkcji `stworz...`, na przykład:

```python
pilka = stworz_pilke()
paletka1 = stworz_paletke()
paletka2 = stworz_paletke()
```

Każda zmienna musi mieć unikalną nazwę.


# Wbudowane zmienne

```python
# klawisze:
gora
dol
w
s

# kolory:
bialy
czarny
czerwony
niebieski
```


# Tworzenie obiektów

```python
<zmienna> = stworz_okno_gry(<wysokosc>, <szerokosc>)
# tworzy okno gry, które jest przechowywane w zmiennej

<zmienna> = stworz_paletke()
# tworzy paletke, która jest przechowywana w zmiennej

<zmienna> = stworz_pilke()
# tworzy pilke, która jest przechowywana w zmiennej
```


# Instrukcje warunkowe

Instrukcje warunkowe są wykonywane za każdym razem, gdy zaistnieje (lub nie) dany warunek. Podając parametry `warunek` lub `instrukcja`, należy wpisać nazwę funkcji **bez** nawiasów `()`, a jej parametry po przecinku (tam, gdzie są `<parametry>`).

```python
jesli(<warunek>, <parametry>).to(<instrukcja>, <parametry>)
# za każdym razem, gdy dany warunek jest prawdziwy, wykonuje instrukcję

jesli(nie(<warunek>, <parametry>)).to(<instrukcja>, <parametry>)
# za każdym razem, gdy nie dany warunek nie jest prawdziwy, wykonuje instrukcję
```


# Warunki

```python
# dla piłek:
dotyka_lewej_sciany()
dotyka_prawej_sciany()
```


# Funkcje

```python
# dla wszystkich obiektów:
przesun_do(<x>, <y>)
ustaw_rozmiary(<szerokość>, <wysokość>)
aktualizuj_stan()
rysuj(<okno>)
ustaw_kolor(<kolor>)

# dla piłek:
przesun_do_gory()
przesun_w_dol()
zwieksz_punkty()

# dla paletek:
ustaw_predkosc(<prędkość>)

# ogólne:
wyswietl_tekst(<okno>, <tekst>, <x>, <y>)
stworz_pilke()
stworz_paletke()
stworz_okno_gry(<wysokosc>, <szerokosc>)
rozpocznij_nowa_runde()
nacisniety_klawisz(<klawisz>)
```

# Stałe cechy

```python
# dla wszystkich obiektów:
zawsze_odbijaj_od_scian()

# dla piłek:
zawsze_odbijaj_od_paletek()
```
