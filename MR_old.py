from random import randrange,getrandbits
from math import log,ceil

def nbit_odd(n):
    if n==1:
        return 1
    return randrange(2**(n-1)+1,2**(n),2)

def is_MRnonwitness(a,n):
    if a==0:
        return True
    s=n-1
    t=0
    while s&1==0: 
        s=s>>1
        t+=1
    u=(a**s)%n 
    if u-1==0 or u+1==n:
        return True
    for i in range(t-1):
        u=(u**2)%n
        if u+1==n:
            return True
    return False

def generate_prime(n): # assert n>1
    assert n>1
    k=ceil(43*log(log(n)))
    while True:
        m=nbit_odd(n)
        find=True
        for i in range(k):
            a=getrandbits(n)%m
            if not is_MRnonwitness(a,m):
                find=False
                break
        if find:  
            return m