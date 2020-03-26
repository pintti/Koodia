suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
test_letters = ['a', 'i', 't', 'n', 'e', 's', 'o', 'h']

def ceasar_sum_brute(alphabet):
    msg = input('Give the encrypted message: ').lower().split(" ")
    while True:
        k = input('Give the k you want to test (blank if quit): ')
        if k == "":
            return
        k = int(k)
        de_message = []

        for word in msg:
            decrypted = []
            for letter in word:
                if letter in alphabet:
                    index = alphabet.index(letter)
                    decoded = index - k
                    while decoded < 0:
                        decoded = decoded + len(alphabet)
                    enword = alphabet[decoded]
                    decrypted.append(enword)
                decryptword = "".join(decrypted).strip(" ")
            de_message.append(decryptword)
        print(" ".join(de_message).upper())


def ceasar_mul_brute(alphabet):
    msg = input('Give the encrypted message: ').lower().split(" ")
    while True:
        x = input('x (blank if quit): ')
        print(x)
        if x == "":
            return
        x = int(x)
        denumber = 0
        r0 = len(alphabet)
        qs = []
        de_message = []
        while x > 0:
            r = int(r0 % x)
            q = int((r0 - r) / x)
            qs.append(q)
            r0 = x
            x = r
        denumber = teet(qs, r0, alphabet)
        if denumber < 0:
            denumber = denumber + len(alphabet)
        for word in msg:
            decrypted = []
            for letter in word:
                if letter in alphabet:
                    index = alphabet.index(letter)
                    decoded = index * denumber
                    while decoded > len(alphabet):
                        decoded = decoded - len(alphabet)
                    decrypted.append(alphabet[decoded])
                decryptionword = "".join(decrypted).strip(" ")
            de_message.append(decryptionword)
        print(" ".join(de_message).upper())    


def teet(qs, t2, alphabet):
    t1 = 0
    i = 0
    t = 0
    while t < len(alphabet):
        t = t1 - (qs[i] * t2)
        if t == len(alphabet) or -t == len(alphabet):
            return t2
        else:
            t1 = t2
            t2 = t
            i = i + 1


def affini_brute(alphabet):
    msg = input('Give the encrypted message: ').lower().strip(" ")
    letters = []
    number = 0
    for letter in alphabet:
        x = msg.count(letter)
        if x > 0:
            if x > number:     
                letters.insert(0, [x, letter])
                number = x
            else:
                letters.append([x, letter])
    big_num, big_ltr = letters.pop(0)

    print('Your most seen letter is {}, which appears {} times.'.format(big_ltr, big_num))
    sec_num = 0
    for instance in letters:
        test_num, test_ltr = instance
        if test_num > sec_num:
            sec_num = test_num
            sec_ltr = test_ltr
    print('Your second most seen letter is {}, which appears {} times.'.format(sec_ltr, sec_num))
    print('Possible combinations using the most used letters:')

    index2 = alphabet.index(sec_ltr)
    index1 = alphabet.index(big_ltr)
    
    print('Comparing your most seen letters to most used letters in the alphabet.')
    big_brute(alphabet, msg, index1, index2, test_letters)

    print('If you did not find the decrypted message, try with every letter in the alphabet? (Y/N)')
    choice = ''
    while choice != 'n':
        choice = input().lower()
        if choice == 'y':
            big_brute(alphabet, msg, index1, index2, alphabet)
            return
        elif choice == 'n':
            return
        else:
            print('Y/N only')

def big_brute(alphabet, msg, index1, index2, letters):
    for letter1 in letters:
        for letter2 in letters:
            try:
                if letter1 == letter2:
                    continue
                print()
                print('Compared letters: {}, {}'.format(letter1, letter2))
                if alphabet.index(letter2) == 0:
                    b = index2
                    c = index1 - b
                    inv_number = solve_inverse_number(len(alphabet), alphabet.index(letter1), alphabet)
                    a = inv_number * c   
                    de_a = -alphabet.index(letter1)
                    de_b = -b * de_a
                    while de_a < 0:
                        de_a = de_a + len(alphabet)
                    while de_b > len(alphabet):
                        de_b = de_b - len(alphabet)
                    word = decrypt(alphabet, msg, de_a, de_b)
                    print("Word: {}, encryption equation: {}*x+{}".format(word, a, b))
                    print('Decryption equation: {}*y+{}'.format(de_a, de_b))

                else:
                    a = alphabet.index(letter1) - alphabet.index(letter2)
                    while a < 0:
                        a += len(alphabet)
                    t = index1 - index2
                    inv_number = solve_inverse_number(len(alphabet), a, alphabet)
                    a = inv_number * t
                    while not 0 < a < len(alphabet):
                        if a < 0:
                            a += len(alphabet)
                        elif a > len(alphabet):
                            a -= len(alphabet)
                        if a == 0:
                            break
                    b = index1 - alphabet.index(letter1) * a 
                    while b < 0:
                        b += len(alphabet)
                    de_a = -a
                    while not 0 < de_a < len(alphabet):
                        if de_a < 0:
                            de_a += len(alphabet)
                        elif de_a > len(alphabet):
                            de_a -= len(alphabet)
                        if de_a == 0:
                            break
                    de_b = -b * de_a
                    while not -len(alphabet) < de_b < len(alphabet):
                        if de_b < 0:
                            de_b += len(alphabet)
                        elif de_b > len(alphabet):
                            de_b -= len(alphabet)
                    word = decrypt(alphabet, msg, de_a, de_b)
                    ab = solve_inverse_number(len(alphabet), de_a, alphabet)
                    print("Word: {}, encryption equation: {}*x+{}".format(word, ab, b))
                    print('Decryption equation: {}*y+{}'.format(de_a, de_b))
                
            except(IndexError):
                print('Unsuccesful.')
                continue


def decrypt(alphabet, msg, inv_number, b):
    decrypt_msg = []
    decrypted = []
    for word in msg:
        for letter in word:
            if letter in alphabet:
                index = alphabet.index(letter)
                decrypt = index * inv_number + b
                while decrypt >= len(alphabet):
                    decrypt = decrypt - len(alphabet)
                decrypted.append(alphabet[decrypt])
            decrypt_wrd = "".join(decrypted)
    return(decrypt_wrd)
            
        
def solve_inverse_number(r0, x, alphabet):
    """solves the inverse number using euclidean algorithm"""
    qs = []
    while x > 0:
        r = int(r0 % x)
        q = int((r0 - r) / x)
        qs.append(q)
        r0 = x
        x = r
    inv_number = teet(qs, r0, alphabet)
    return inv_number


language = input('Choose either (f)innish or (e)nglish alphabet: ')
alphabet = english
if language == 'f':
    alphabet = suomi
elif language == 'e':
    alphabet = english
else:
    print('English has been chosen by default')
print('Choose what kind of encryption you want to brute force')
choice = input('Ceasar (s)um, Ceasar (m)ultiplier or (a)ffini: ')
if choice == 's':
    ceasar_sum_brute(alphabet)
elif choice == 'm':
    ceasar_mul_brute(alphabet)
elif choice == 'a':
    affini_brute(alphabet)
else:
    print('No function selected, terminating')
input()
