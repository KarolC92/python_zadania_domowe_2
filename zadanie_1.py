# ### Zadanie 3.1 Funkcje liczbowe

# Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

# 1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
# 2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
# 3. `srednia` - oblicza średnią z dwóch liczb,
# 4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
# podpowiedź: wartość PI jest dostępna jako `Math.PI`
# 5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
# 6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
# 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
# 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

# Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.

def stopy_na_metry(x: float) -> float:
    return f'{x} ft = {(x * 0.3048):.4f} m.'


print(stopy_na_metry(9))


def max_liczba(a: int, b: int) -> str:
    if a > b:
        return f'Większa z pary: ({a}, {b}) to: {a}'
    elif b > a:
        return f'Większa z pary: ({a}, {b}) to: {b}'
    else:
        return 'Obie liczby są równe'


print(max_liczba(4, 8))


def srednia(a, b):
    return f'Średnia liczb ({a}, {b}) = {((a + b) / 2):.2f}'


print(srednia(2, 9))

import math


def pole_kola(r):
    return f'Pola koła o promieniu {r} = {(math.pi * r ** 2):.2f} j^2'


print(pole_kola(78))


def bmi(masa: float, wzrost: float) -> str:
    return f'Bmi dla wzrostu {wzrost} cm i masie ciała {masa} kg wynosi: {(masa / (wzrost / 100) ** 2):.2f}'


print(bmi(72, 178))


def pola_trojkata(a, b, c):
    try:
        wynik = round(math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4, 2)
        if wynik > 0:
            return f'Pole trójkąta wynosi: {wynik}'
        else:
            return f'Z podanych boków nie można utworzyć trójkąta!'
    except ValueError:
        return f'Z podanych boków nie można utworzyć trójkąta!'


print(pola_trojkata(1, 4, 4))


def kilometry_na_mile(a):
    return f'{a} km = {a * 0.621371192:.2f} mili.'


print(kilometry_na_mile(5))


def mile_na_kilometry(a):
    return f'{a} mil = {a * 1.609344:.2f} km.'


print(mile_na_kilometry(5))
