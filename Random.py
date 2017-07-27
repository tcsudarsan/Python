'''
Created on 9 Mar 2017

@author: sudarsan
'''
from __builtin__ import range
def Factorial(num):
    b=1
    if (num==0):
        print("Factorial of "+str(num)+"is 1")
    else:
        for i in range(1,num+1):
             
            b=b*i
            
    print ("factorial of "+str(num)+" is "+str(b))
    
Factorial(0)    
        