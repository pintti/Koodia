from itertools import permutations
from collections import Counter

"""Ringissä istuu 5 pelaajaa. Jokaiselle pelaajalle jaetaan 6 kortin pakasta kortti, jotka osoittavat seuraavia pelaajia:
-Kortin haltijan vasemmalla puolella oleva pelaaja.
-Toinen pelaaja kortin haltijan vasemmalla puolella.
-Toinen pelaaja kortin haltijan vasemmalla puolella.
-Kortin haltijan oikealla puolella oleva pelaaja.
-Toinen pelaaja kortin haltijan oikealla puolella.
-Toinen pelaaja kortin haltijan oikealla puolella.
(yksi kortti jää yli)
Millä todennäköisyydellä yhtä ringissä istuvaa pelaajaa osoittaa vähintään 3 korttia? Ja sitten 4 korttia?"""

cards = [1, 2, 2, -1, -2, -2]
perms = permutations(cards, 5)
possibilities = 0
successes_3 = 0
successes_4 = 0

for perm in perms:
    player_nums = []
    for player_place, card in enumerate(perm):
        player_num = player_place + card
        if player_num > 4:
            player_num -= 5
        if player_num < 0:
            player_num += 5
        player_nums.append(player_num)
    for i in range(0, 5):
        if player_nums.count(i) == 3:
            successes_3 += 1
            print(perm, player_nums)
        if player_nums.count(i) == 4:
            successes_4 += 1
            print(perm)
    possibilities += 1
print(possibilities, successes_3, successes_4)
print(successes_3 / possibilities)
print(successes_4 / possibilities)
