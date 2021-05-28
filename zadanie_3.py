# ### Zadanie 3.3 | Operacje na listach

# Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb
# i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.

# ```
# lista_liczb = [10, 20, 30, 40]
# wynik = suma(lista_liczb)
# ```
# - `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
# - `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
# - `max(liczby)` – zwraca największą wartość z listy
# `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
# - `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
# - `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
# - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w
# `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`,
# które są podzielne przez `x`
# - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w
# `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście
# `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma

lista_liczb = [10, 20, 30, 40]


def suma(liczby: list):
    wynik = 0
    for i in liczby:
        wynik += i
    return wynik


def srednia(liczby: list):
    s = suma(liczby)
    wynik = s / len(liczby)
    return wynik


def max(liczby: list):
    wynik = None
    for i in liczby:
        if wynik == None:
            wynik = i
        elif i > wynik:
            wynik = i
    return wynik


def roznica_min_max(liczby: list):
    minimum = None
    if len(liczby) > 0:
        for i in liczby:
            if minimum == None:
                minimum = i
            elif i < minimum:
                minimum = i
        return max(liczby) - minimum
    else:
        return 0


def wypisz_wieksze(liczby: list, a: int):
    wieksze = []
    for i in liczby:
        if i > a:
            wieksze.append(i)
    return wieksze


def pierwsza_wieksza(liczby: list, a: int):
    if len(wypisz_wieksze(liczby, a)) > 0:
        return wypisz_wieksze(liczby, a)[0]
    else:
        return None


def suma_wieszych(liczby: list, a: int):
    return sum(wypisz_wieksze(liczby, a))


def ile_wiekszych(liczby: list, a: int):
    return len(wypisz_wieksze(liczby, a))


def wypisz_podzielne(liczby: list, a: int):
    wynik = []
    for i in liczby:
        if i % a == 0:
            wynik.append(i)
    return wynik


def pierwsza_podzielna(liczby: list, a: int):
    if len(wypisz_podzielne(liczby, a)) > 0:
        return wypisz_podzielne(liczby, a)[0]
    else:
        return None


def znajdz_wspolny(liczby1: list, liczby2: list):
    if set(liczby1) & set(liczby2) != set():
        return set(liczby1) & set(liczby2)
    else:
        return None


print(suma(lista_liczb))
print(srednia(lista_liczb))
print(max(lista_liczb))
print(roznica_min_max(lista_liczb))
print(wypisz_wieksze(lista_liczb, 20))
print(pierwsza_wieksza(lista_liczb, 10))
print(suma_wieszych(lista_liczb, 20))
print(ile_wiekszych(lista_liczb, 20))
print(wypisz_podzielne(lista_liczb, 5))
print(pierwsza_podzielna(lista_liczb, 5))
print(znajdz_wspolny(lista_liczb, [20, 90]))
