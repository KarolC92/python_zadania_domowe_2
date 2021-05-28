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

    :param data: Lista, z której zamierzamy uzyskać wycinek
    :param start: Wartość, powyżej której rozpoczynamy przypisywanie wartości z listy początkowej do wycinka
    :param stop: Największa wartość, która może zostać przypisana do wycinka z listy początkowej
    :return: Wycinek listy, gdzie: min(wycinek) > start, max(wycinek) = stop
    """
    a = list(filter(lambda x: start < x <= stop, data))
    return a

print(przytnij([1, 2, 3, 4, 5, 6, 7], 3, 6))

