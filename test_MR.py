from test import *
from MR import *

t=Test()

def test_nbit_odd(data):
    out=nbit_odd(*data)
    if out%2==0:
        return False
    
    n=data[0]
    for i in range(n-1):
        out//=2
    if out>2:
        return False
    out//=2
    if out!=0:
        return False
    return True
t.regist(nbit_odd)
t.regist(test_nbit_odd)
t.add(nbit_odd,[10])
t.add(nbit_odd,[1024])


t.regist(is_MRnonwitness)
t.add(is_MRnonwitness,[6,7,True])
t.add(is_MRnonwitness,[2,101,True])
t.add(is_MRnonwitness,[4,101,True])
t.add(is_MRnonwitness,[66,101,True])
t.add(is_MRnonwitness,[67,101,True])
t.add(is_MRnonwitness,[3,25,False])


        
def test_generate_prime(data):
    out=generate_prime(*data)
    if data[0]==1:
        return False
    elif data[0]==2:
        if out in [3]:
            return True
    elif data[0]==3:
        if out in [5,7]:
            return True
    elif data[0]==4:
        if out in [11,13]:
            return True
    else:
        return True
    return False
        
t.regist(generate_prime)
t.regist(test_generate_prime)
t.add(generate_prime,[2])
t.add(generate_prime,[3])
t.add(generate_prime,[4])

t.test()