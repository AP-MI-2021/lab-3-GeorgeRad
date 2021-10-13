# Functia de calcul pentru problema 5
# Verificam daca un element este palindrom sau nu
def is_palindrome(n):
    """
    Verificam daca un numar intreg este palindrom
    :param n: numar intreg
    :return: True sau False
    """
    clone_n = n
    oglindit = 0
    while clone_n > 0:
        oglindit = oglindit * 10 + clone_n % 10
        clone_n = clone_n // 10
    if n == oglindit:
        return True
    return False


# Functia de test pentru is_palindrome
def test_is_palindrome():
    assert is_palindrome(1221) is True
    assert is_palindrome(13431) is True
    assert is_palindrome(66466) is True
    assert is_palindrome(123) is False
    assert is_palindrome(64) is False


# Functie de calcul pentru problema 5
# Determinam daca o lista data este formata doar din palindroame
def all_list_is_formed_with_palindromes(lista):
    """
    Verificam daca o lista este formata doar din palindroame
    :param lista: lista de numere intregi
    :return: True sau False
    """
    for i in lista:
        if is_palindrome(i) is False:
            return False
    return True


# Functie de test pentru all_list_is_formed_with_palindromes
def test_all_list_is_formed_with_palindromes():
    assert all_list_is_formed_with_palindromes([121, 232, 343]) is True
    assert all_list_is_formed_with_palindromes([646, 132, 2321]) is False
    assert all_list_is_formed_with_palindromes([134234, 2132, 1223]) is False

# Problema 5 (Functie de calcul)
# Functia care determina cea mai lunga subsecventa de palindroame dintr-o lista
def get_longest_all_palindromes(lista):
    """
    Cautarea celei mai lungi secvente de numere care sunt palindroame
    :param lista: lista de numere intregi
    :return: secventa de numere intregi
    """
    subsecventa_maxima = []
    lungime_lista = len(lista)
    for i in range(lungime_lista):
        for j in range(i, lungime_lista):
            if all_list_is_formed_with_palindromes(lista[i:j + 1]) and len(lista[i: j + 1]) > len(subsecventa_maxima):
                subsecventa_maxima = lista[i: j + 1]
    return subsecventa_maxima


# Functia de test pentru get_longest_all_palindromes
def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([1221, 1441, 45, 23]) == [1221, 1441]
    assert get_longest_all_palindromes([64, 23, 34, 96, 13]) == []
    assert get_longest_all_palindromes([1221, 1441, 345, 1551, 1661, 1771, 1991]) == [1551, 1661, 1771, 1991]

# Problema13
# Functie de calcul
# Functie care verifica daca o lista este compusa din numere formate din cifre prime
# Ne va ajuta in cautarea celei mai lungi subsecvente de numere formate doar din cifre prime
def list_is_formed_with_primes_digits(lista):
    """
    Verificam daca o lista data contine doar elemente formate din numere prime
    :param lista: lista de numere intregi
    :return: True sau False
    """
    for i in lista:
        while i > 0:
            if i % 10 != 2 and i % 10 != 3 and i % 10 != 5 and i % 10 != 7:
                return False
            i = i // 10
    return True

# Functia de test pentru list_is_formed_with_primes_digits
def test_list_is_formed_with_primes_digits():
    assert list_is_formed_with_primes_digits([235, 357]) is True
    assert list_is_formed_with_primes_digits([223, 332, 1223]) is False
    assert list_is_formed_with_primes_digits([1223, 23123, 32, 67]) is False

# Problema 13
# Functie de calcul
# Functia care cauta cea mai lunga subsecventa de numere formate din cifre prime
def get_longest_prime_digits(lista):
    """
    Cautam cea mai lunga secventa compusa din numere formate din cifre prime
    :param lista: lista de numere intregi
    :return: cea mai lunga secventa, prin lista "subsecventa_maxima"
    """
    subsecventa_maxima = []
    lungime_lista = len(lista)
    for i in range(lungime_lista):
        for j in range(i, lungime_lista):
            if list_is_formed_with_primes_digits(lista[i: j + 1]) is True and len(lista[i: j + 1]) > len(subsecventa_maxima):
                subsecventa_maxima = lista[i: j + 1]
    return subsecventa_maxima


# Functia de test pentru get_longest_prime_digits
def test_get_longest_prime_digits():
    assert get_longest_prime_digits([22, 33, 12, 77, 55, 33]) == [77, 55, 33]
    assert get_longest_prime_digits([22, 33, 12, 11, 34, 55, 779, 29573]) == [22, 33]
    assert get_longest_prime_digits([123, 234, 345, 567]) == []


# Functia care va test toate functiile mele
def test_all_functions():
    test_is_palindrome()
    test_all_list_is_formed_with_palindromes()
    test_get_longest_all_palindromes()
    test_list_is_formed_with_primes_digits()
    test_get_longest_prime_digits()

test_all_functions() # Testam toate functiile

def menu():
    print("5. Cautarea celei mai lungi subsecvente de numere care sunt palindroame")
    print("13. Cauta cea mai lunga subsecventa de numere formate doar din cifre prime")


def read_the_list():
    """
    Functie pentru citirea unei liste
    :return: lista de numere intregi citita
    """
    n = int(input("Introduceti numarul elementelor listei: "))
    print("(Introduceti elementele unu sub celalalt cu Enter)")
    lista = []
    number = 0
    for i in range(n):
        number = int(input())
        lista.append(number)
    return lista


menu()
optiune = int(input("Introduceti optiunea dumneavoastra: "))
ok = True
while ok:
    lista = []
    if optiune == 5:
        lista = read_the_list()
        print("Cea mai lunga secventa de palindroame este: ", get_longest_all_palindromes(lista))
    elif optiune == 13:
        lista = read_the_list()
        print("Cea mai lunga secventa de numere compuse din cifre prime este: ", get_longest_prime_digits(lista))
    print()
    print("Doriti sa mai introduceti optiuni?")
    raspuns = input("Raspundeti cu DA sau NU ")
    if raspuns == "NU":
        ok = False
    elif raspuns == "DA":
        print()
        print()
        menu()
        print()
        optiune = int(input("Introduceti optiunea dumneavoastra: "))






