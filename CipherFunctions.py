import string 
import random



# ============= Caesar Cipher =============
CAESAR_SHIFT = 5 

lower = string.ascii_lowercase
upper = string.ascii_uppercase
shifted_lower = lower[CAESAR_SHIFT:] + lower[:CAESAR_SHIFT]
shifted_upper = upper[CAESAR_SHIFT:] + upper[:CAESAR_SHIFT]

CAESAR_ENCRYPT_DICT = dict(zip(lower + upper, shifted_lower + shifted_upper))
CAESAR_DECRYPT_DICT = dict(zip(shifted_lower + shifted_upper, lower + upper))

    
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
substitution_lower = list(string.ascii_lowercase)
substitution_upper = list(string.ascii_uppercase)
random.shuffle(substitution_lower)
random.shuffle(substitution_upper)

SUBSTITUTION_ENCRYPT_DICT = dict(zip(lower + upper, substitution_lower + substitution_upper))
SUBSTITUTION_DECRYPT_DICT = dict(zip(substitution_lower + substitution_upper, lower + upper))

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