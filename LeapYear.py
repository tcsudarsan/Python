'''
Created on 15 Mar 2017

@author: sudarsan
'''
class FindLeapYear:
    def FindLY(self,year):
        if((year%4==0)and ((year/100)%4==0)):
            
            print(str(year)+" is a leap year")
        else:
            print(str(year)+" is not a leap year")
b=FindLeapYear()
a=2300
b.FindLY(a)

        