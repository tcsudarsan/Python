'''
Created on 15 Mar 2017

@author: sudarsan
'''
class FindGreatNo:
    def GreatNo(self,a,b,c):
        if(a>b and a>c):
            print(str(a)+" is greater")
        elif(b>c and b>a):
            print(str(b)+" is greater")
        elif(c>a and c>b):
            print(str(c)+" is greater")
d=FindGreatNo()
a=25
b=23
c=24
d.GreatNo(a,b,c)
    