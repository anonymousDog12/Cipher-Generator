from test import Test
from CipherFunctions import *
t=Test()
def test_EE(data):
    a,b=data
    d,s,t=EE(*data)
    return d==a*s+b*t and a%d==0 and b%d==0
    
t.regist(EE)
t.regist(test_EE)
t.add(EE,[8,12])
t.add(EE,[1,0])
t.add(EE,[36782,432])
t.add(EE,[-4,18])

def test_RSA(data):
    N=10
    n,e,d=RSA(*data)
    for k in range(N):
        a=randrange(1,n,2)
        if not pow(pow(a,e,n),d,n)==a:
            return False
    return True
t.regist(RSA)
t.regist(test_RSA)
t.add(RSA,[10])
t.add(RSA,[20])
t.add(RSA,[40])
t.add(RSA,[512])

t.test()