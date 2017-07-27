'''
Created on 17 Mar 2017

@author: sudarsan
'''
import webbrowser
import time
NoOfBreak=5
count=0
while(count<NoOfBreak):
    time.sleep(30)
    print("program is started at"+time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=zggQw2wb60M")
    count=count+1