
# t=Test()
# #usage 1: t.test(my_fun) will compare if my_fun(var1,var2,...)==exp_output  
# def my_fun(var1,var2,...):
#     something()
#     return output
# t.regist(my_fun)
# t.add(my_fun,[var1,var2,...,exp_output])
# t.test(my_fun)
# #usage 2: t.test(myfun) will pass if test_my_fun2(var1,var2,...) is True
# #test_my_fun must return a bool value
# def my_fun2(var1,var2,...):
#     something()
#     return output
# t.regist(my_fun2)
# t.regist(test_myfun2)
# t.add(my_fun2,[var1,var2,...])
# t.test(my_fun2)
##usage 3: test() will test all the registed functions
#t.test()

import types
from random import randrange,getrandbits
from math import log,ceil
from inspect import signature
import re
import os

class Test:#designed to test function with fixed number of arugument and with non-empty return.
    
    
    tested_funs={}
    tester_funs={}
    data={}#format fun_name:a list of teset data,with the expected result at the end(if any) 
    
    def __init__(self):
        self.data={}
        self.tested_funs={}
        self.tester_funs={}
    def list(self):
        print(self.tested_funs)
        print(self.tester_funs)
        print(self.data)
    def regist(self,fun):
        if re.match(r'test_',fun.__name__):
            self.tester_funs[fun.__name__]=fun
        else:
            self.tested_funs[fun.__name__]=fun
            self.data[fun.__name__]=[]
            self.tester_gen(fun)
    
    def test_equal(self,true_output,test_output):
        return true_output==test_output

    def tester_gen(self,fun):
        if not ('test_'+fun.__name__ in self.tester_funs):
            self.tester_funs['test_'+fun.__name__]=self.test_equal
    def add(self,fun,data):
        assert fun.__name__ in self.tested_funs
        if self.data[fun.__name__]:
            assert len(self.data[fun.__name__][-1])==len(data)
        self.data[fun.__name__].append(data)
            
    def test(self,tested_funs=None):
        
        if not tested_funs:
            tested_funs=self.tested_funs
        if isinstance(tested_funs,types.FunctionType):
            tested_funs=[tested_funs.__name__]
       
        for fun_name in tested_funs:
            logs=[]
            error=False
            para=signature(self.tested_funs[fun_name]).parameters
            print('testing '+fun_name)
            for test_data in self.data[fun_name]:
                if len(test_data)==len(para):
                   
                    if not self.tester_funs['test_'+fun_name](test_data):
                        error=True
                        logs.append("function "+fun_name+' has error with input '+str(test_data)+' and output'+str(self.tested_funs[fun_name](*test_data)))
                elif len(test_data)==len(para)+1:
                    true_output=self.tested_funs[fun_name](*test_data[:-1])
                    if not self.tester_funs['test_'+fun_name](test_data[-1],true_output):
                        error=True
                        logs.append("function "+fun_name+' has error with input '+str(test_data)+' and output '+str(true_output))
                else:
                    print(papa)
                    print(test_data)
                    assert 1==0
            if not error:
                logs.append("function "+fun_name+' passed unit test')
            for log in logs:
                print(log)      
