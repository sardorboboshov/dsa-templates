from string import ascii_lowercase, ascii_uppercase
from collections import defaultdict
vowels = 'aeiou'
non_vowels = list(sorted(set(ascii_lowercase) - set(vowels)))
non_vowels = "".join(non_vowels)
v1 = ascii_lowercase
v2 = ascii_uppercase
v1_vowels = 'aeiou'
v2_vowels = 'AEIOU'
v1_consonant = list(sorted(set(ascii_lowercase) - set(v1_vowels)))
v2_consonant = list(sorted(set(ascii_uppercase) - set(v2_vowels)))
v12_vowels = v1_vowels + v2_vowels
v12_consonant = v1_consonant + v2_consonant
# print(v1_consonant, v2_consonant, v12_consonant)

