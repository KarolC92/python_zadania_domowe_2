# ### Zadanie 3.2 | Miesiące

# Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
# Logikę obliczania liczby dni wydziel do osobnej funkcji.

# **Wersja A**
# Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.

# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.

from calendar import monthrange

miesiace = {'styczeń': 1,
            'luty': 2,
            'marzec': 3,
            'kwiecień': 4,
            'maj': 5,
            'czerwiec': 6,
            'lipiec': 7,
            'sierpień': 8,
            'wrzesień': 9,
            'październik': 10,
            'listopad': 11,
            'grudzień': 12,
            }


def dni_miesiaca(a, r):
    try:
        return monthrange(int(r), miesiace[a])[1]
    except KeyError:
        return f'Niewłaściwy miesiąc'


rok = 2021
miesiac = input("Podaj nazwę miesiąca: ")

if miesiac in miesiace:
    if miesiac == 'luty':
        try:
            rok = input("podaj rok: ")
            print(f'Liczba dni w miesiącu: "{miesiac}" na rok {rok} wynosi: {dni_miesiaca(miesiac, rok)}.')
        except ValueError:
            print('Niepoprawne dane!')
    else:
        print(f'Liczba dni w miesiącu: "{miesiac}" wynosi: {dni_miesiaca(miesiac, rok)}.')
else:
    print('Niepoprawne dane!')



