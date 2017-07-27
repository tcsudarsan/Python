'''
Created on 8 Mar 2017

@author: sudarsan
'''
class Swap:
    def Swapping(self):
        a =[]
        i=3
        while(i>0):
            b=input("enter no into list: ")
            a.append(b)
            i=i-1
        print "array before swapping:"
        print a
        b=a[2]
        a[2]=a[0]
        a[0]=a[1]
        a[1]=b    
        print "array after swapping:"
        print a
new=Swap()
new.Swapping()