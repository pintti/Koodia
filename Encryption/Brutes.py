suomi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'å', 'ä', 'ö']
english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

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
                    if decoded < 0:
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
    msg = input('Give the encrypted message: ').lower()
    letters = [[],[]]
    print(msg)
    for letter in alphabet:
        x = msg.count(letter)
        if x > 0:
            letters[0].append(letter)
            letters[1].append(x)
    for instance in letters:
        print(instance)
        



affini_brute(suomi)