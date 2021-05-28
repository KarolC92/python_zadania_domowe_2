# ### Zadanie 3.4 | Przycinanie listy

# Zaimplementuj funkcję przycinającą listę na podstawie podanego warunku początkowego oraz końcowego:
# Przykład użycia:
#
# > przytnij(
# data = [1, 2, 3, 4, 5, 6, 7],
# start = lambda x: x > 3,
# stop = lambda x: x == 6,
# )
#
# [4, 5, 6]


def przytnij(data: list, start: int, stop: int) -> list:
    """
    Funkcja zwracająca wycinek listy: data

    :param data: Lista, z której zamierzamy uzyskać konkretny wycinek
    :param start: Indeks, pod którym znajduje się element, powyżej którego rozpoczynamy wycinanie listy
    :param stop: Indeks, pod którym znajduje się ostatni element z listy przypisany do naszego "wycinka"
    :return: "Wycinek": data[start + 1: stop]
    """
    a = list(filter(lambda x: x > start, data))
    b = list(filter(lambda x: x <= stop, a))
    return b

print(przytnij([1, 2, 3, 4, 5, 6, 7], 3, 6))
