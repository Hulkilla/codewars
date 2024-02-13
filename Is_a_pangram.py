import numpy as np
alphabet = "abcdefghijklmnopqrstuvwxyz"
letters_array = list(alphabet)

study = "Cwm fjord bank glyphs vext quiz"
study.lower()
study = "".join(x for x in study if x in alphabet)
letters_study = sorted(list(set(study)))

# Ejemplo de uso:

if letters_array == letters_study: 
    print(True)
else:
    print(False)


import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True