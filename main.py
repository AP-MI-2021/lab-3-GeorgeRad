# Problema 6

# Functie de calcul pentru problema 6
def all_elements_div_k(lista, k):
    """
    Verificam daca o lista data are toate elementele divizibile cu k
    :param lista: o lista de numere intregi
    :param k: numar intreg
    :return: True sau False
    """
    for i in lista:
        if i % k != 0:
            return False
    return True

# Functia de test pentru functia all_elements_div_k
def test_all_elements_div_k():
    assert all_elements_div_k([24, 12, 36], 2) is True
    assert all_elements_div_k([33, 44, 55], 11) is True
    assert all_elements_div_k([12, 34, 55, 69], 2) is False

# Functia care cauta cea mai lunga secventa divizibila cu k
def get_longest_div_k(lst, k):
    """
    Cautam cea mai lunga secventa de numere divizibile cu k
    :param lst: o lista de numere intregi
    :param k: numar intreg
    :return: lista subsecventa_maxima formata din numere intregi
    """
    secventa_maxima = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_elements_div_k(lst[i: j + 1], k) is True and len(lst[i: j + 1]) > len(secventa_maxima):
                secventa_maxima = lst[i: j + 1]
    return secventa_maxima


# Functia de test pentru functia get_longest_div_k
def test_get_longest_div_k():
    assert get_longest_div_k([4, 6, 5, 8, 10, 12], 2) == [8, 10, 12]
    assert get_longest_div_k([1, 2, 4, 8, 7, 5], 2) == [1, 2, 4, 8]
    assert get_longest_div_k([23, 23], 8) == []


# Functie care testeaza toate testele
def test_all():
    test_all_elements_div_k()
    test_get_longest_div_k()

# Meniul Programului
def menu():
    print("6. Cauta cea mai lunga secventa de numere divizibile ,dintr-o lista data, cu un k dat ")


# Functie de citire a unei liste
def read_the_list():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l


def main():
    lst = []
    menu()
    optiune = int(input("Introduceti optiunea dumneavoastra: "))
    while True:
        if optiune == 6:
            k = int(input("Introduceti k = "))
            lst = read_the_list()
            print(get_longest_div_k(lst, k))
        raspuns = input("Doriti sa mai introduceti optiuni? ")
        if raspuns == "DA" or raspuns == "da":
            print()
            menu()
            optiune = int(input("Introduceti optiunea dumneavoastra: "))
        elif raspuns == "NU" or raspuns == "nu":
            break

main()

