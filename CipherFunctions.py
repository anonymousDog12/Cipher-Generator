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
    
#=================== RSA cipher=====================

from MR import generate_prime
from random import randrange
from math import gcd


CH_BOUND=146

def RSA(K):#generate a K bit n as key
    assert (K>3)
    
    p=generate_prime(K//2+1)
    q=generate_prime(K//2+1)
    while q==p:
        q=generate_prime(K//2+1)
    n=p*q
    e=randrange(1,n,2)
    while(gcd(e,(p-1)*(q-1))!=1):
        e=randrange(1,n,2)
    phi=(p-1)*(q-1)
    #print(phi)
    d=EE(e,phi)[1]
    if d<0:
        d+=phi
    return n,e,d

def EE(a,b):
    r0,r1=a,b 
    s0,s1=1,0
    t0,t1=0,1
    if r1==0:
        return abs(a),1,0
    
    q1,r2=divmod(r0,r1)
    s2=s0-s1*q1
    t2=t0-t1*q1
    
    while(r2!=0):
        r1,r0=r2,r1
        s1,s0=s2,s1
        t1,t0=t2,t1
        q1,r2=divmod(r0,r1)
        s2=s0-s1*q1
        t2=t0-t1*q1        
    return r1,s1,t1

def RSA_encrypt(text,n,e):
    if len(text)>CH_BOUND:
        return "Out of text bound, "+str(len(text))+" characters were input"
    return str(pow(str2num(text),e,n))


def RSA_decrypt(text,n,d):
    return num2str(pow(int(text),d,n))

def str2num(text):
    num=0
    N=128
    for x in text:
        num*=N
        num+=ord(x)
    return num

def num2str(num):
    N=128
    text=''
    while num!=0:
        text+=chr(num%N)
        num//=N
    return text[::-1]