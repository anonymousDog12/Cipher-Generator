import string 
import random


lower_str = string.ascii_lowercase
upper_str = string.ascii_uppercase
lower_lst = list(lower_str)
upper_lst = list(upper_str)

# ============= Caesar Cipher =============
CAESAR_SHIFT = 5 

shifted_lower = lower_str[CAESAR_SHIFT:] + lower_str[:CAESAR_SHIFT]
shifted_upper = upper_str[CAESAR_SHIFT:] + upper_str[:CAESAR_SHIFT]

CAESAR_ENCRYPT_DICT = dict(zip(lower_str + upper_str, shifted_lower + shifted_upper))
CAESAR_DECRYPT_DICT = dict(zip(shifted_lower + shifted_upper, lower_str + upper_str))

    
def Caesar_encrypt(text):
    res = ""
    for char in text: 
        if char in CAESAR_ENCRYPT_DICT:
            res += CAESAR_ENCRYPT_DICT[char]
        else:
            res += char
    return res

def Caesar_decrypt(text):
    res = ""
    for char in text: 
        if char in CAESAR_DECRYPT_DICT:
            res += CAESAR_DECRYPT_DICT[char]
        else:
            res += char
    return res


# ============= Substitution Cipher =============
substitution_lower = lower_lst[:]
substitution_upper = upper_lst[:]
random.shuffle(substitution_lower)
random.shuffle(substitution_upper)

SUBSTITUTION_ENCRYPT_DICT = dict(zip(lower_lst + upper_lst, substitution_lower + substitution_upper))
SUBSTITUTION_DECRYPT_DICT = dict(zip(substitution_lower + substitution_upper, lower_lst + upper_lst))

def Substitution_encrypt(text): 
    res = ""
    for char in text: 
        if char in SUBSTITUTION_ENCRYPT_DICT:
            res += SUBSTITUTION_ENCRYPT_DICT[char]
        else:
            res += char
    return res

def Substitution_decrypt(text): 
    res = ""
    for char in text: 
        if char in SUBSTITUTION_DECRYPT_DICT:
            res += SUBSTITUTION_DECRYPT_DICT[char]
        else:
            res += char
    return res


# ============= Atbash Cipher =============
atbash_lower = lower_lst[:]
atbash_upper = upper_lst[:]

atbash_lower.reverse()
atbash_upper.reverse()

ATBASH_ENCRYPT_DICT = dict(zip(lower_lst + upper_lst, atbash_lower + atbash_upper))
ATBASH_DECRYPT_DICT = dict(zip(atbash_lower + atbash_upper, lower_lst + upper_lst))

def Atbash_encrypt(text):
    res = ""
    for char in text:
        if char in ATBASH_ENCRYPT_DICT:
            res += ATBASH_ENCRYPT_DICT[char]
        else:
            res += char
    return res

def Atbash_decrypt(text):
    res = "" 
    for char in text: 
        if char in ATBASH_DECRYPT_DICT:
            res += ATBASH_DECRYPT_DICT[char]
        else:
            res += char
    return res


# ============= ROT13 Cipher =============
rot13_shifted_lower = lower_str[13:] + lower_str[:13]
rot13_shifted_upper = upper_str[13:] + upper_str[:13]

ROT13_ENCRYPT_DICT = dict(zip(lower_str + upper_str, rot13_shifted_lower + rot13_shifted_upper))
ROT13_DECRYPT_DICT = dict(zip(rot13_shifted_lower + rot13_shifted_upper, lower_str + upper_str))

    
def Rot13_encrypt(text):
    res = ""
    for char in text: 
        if char in ROT13_ENCRYPT_DICT:
            res += ROT13_ENCRYPT_DICT[char]
        else:
            res += char
    return res

def Rot13_decrypt(text):
    res = ""
    for char in text: 
        if char in ROT13_DECRYPT_DICT:
            res += ROT13_DECRYPT_DICT[char]
        else:
            res += char
    return res

# ============= Baconian Cipher =============
baconian_values = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa',
                   'aabab', 'aabba', 'aabbb', 'abaaa', 'abaaa',
                   'abaab', 'ababa', 'ababb', 'abbaa', 'abbab',
                   'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba',
                   'baabb', 'baabb', 'babaa', 'babab', 'babba',
                   'babbb',
                   'AAAAA', 'AAAAB', 'AAABA', 'AAABB', 'AABAA',
                   'AABAB', 'AABBA', 'AABBB', 'ABAAA', 'ABAAA',
                   'ABAAB', 'ABABA', 'ABABB', 'ABBAA', 'ABBAB',
                   'ABBBA', 'ABBBB', 'BAAAA', 'BAAAB', 'BAABA',
                   'BAABB', 'BAABB', 'BABAA', 'BABAB', 'BABBA', 
                   'BABBB']

BACONIAN_ENCRYPT_DICT = dict(zip(lower_lst + upper_lst, baconian_values))
BACONIAN_DECRYPT_DICT = dict(zip(baconian_values, lower_lst + upper_lst))

def Baconian_encrypt(text):
    res = ""
    res = ""
    for char in text: 
        if char in BACONIAN_ENCRYPT_DICT:
            res += BACONIAN_ENCRYPT_DICT[char]
        else:
            res += char
    return res

def Baconian_decrypt(text):
    res = ""
    for char in text: 
        if char in BACONIAN_DECRYPT_DICT:
            res += BACONIAN_DECRYPT_DICT[char]
        else:
            res += char
    return res
    