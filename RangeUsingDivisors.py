'''
Created on 8 Mar 2017

@author: sudarsan
'''
a=input("enter your number: ")
c=[]
x=range(2,a)
for num in x:
    
    if (a%num==0):
        c.append(num)
c.append(1)
c.append(a)
print ("divisors are: ")
for d in c:
    print d        
