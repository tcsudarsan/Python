'''
Created on 8 Mar 2017

@author: sudarsan
'''
a=[1,2,3,45,23,35,10,7,8,9,17,18,5,6,4,90]
c=[]
for b in a:
    if(b<10):
        c.append(b)
print c.__len__()
print c