suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def teet(qs, t2, z):
    t1 = 0
    i = 0
    t = 0
    while t < z:
        t = t1 - (qs[i] * t2)
        if t == z or -t == z:
            return t2
        else:
            t1 = t2
            t2 = t
            i = i + 1


def solve_inverse_number(r0, x):
    """solves the inverse number using euclidean algorithm"""
    qs = []
    r_og = r0
    while x > 0:
        r = int(r0 % x)
        q = int((r0 - r) / x)
        qs.append(q)
        r0 = x
        x = r
    inv_number = teet(qs, r0, r_og)
    return inv_number


def solve_starting_number(a_length, z):
    k = 0
    M = a_length - 1
    while M < z:
        k += 1
        M += (a_length - 1) * 10**(2*k)
    return k


def turn_word_to_numbers(word, alphabet, k):
    i = 1
    number_list = []
    while i < len(word):
        number = 0
        for p in range(i-1, i+k-1):
            number += alphabet.index(word[p]) * 10**(2*(i-p))
        number_list.append(number)
        i += k
    return number_list


def affini_letter_change(a, b, ln):
    return a * ln + b


def count_number_down(number, z):
    while number > z:
        number -= z
    return number


def turn_number_to_word(alphabet, lista, k):
    word = []
    print(lista)
    for numbers in lista:
        for i in range(k):
            number = numbers[]
    return word


def slice_ecnrypt_method(alphabet, word, z, a, b):
    k = solve_starting_number(len(alphabet), z)
    number_list = turn_word_to_numbers(word, alphabet, k)
    for i, number in enumerate(number_list):
        nu_number = count_number_down(affini_letter_change(a, b, number), z)
        number_list[i] = str(nu_number).zfill(k*2)
    nu_word = turn_number_to_word(alphabet, number_list, k)
    print(nu_word)
    

slice_ecnrypt_method(english, 'takeitaway', 2773, 17, 329)
    
        

