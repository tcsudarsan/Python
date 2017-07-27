'''
Created on 8 Mar 2017

@author: sudarsan
'''
a=[]
i=10
while(i>0):
    b=input("enter a number")
    if(b<10):
        a.append(b)
        i=i-1  
print a.__len__()
print a
 
