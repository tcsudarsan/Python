'''
Created on 19 Mar 2017

@author: sudarsan
'''
from turtle import *
canvas = Screen()
canvas.setup(400,200)

sarah = Turtle()
sarah.forward(50)          # make sarah draw a square
sarah.left(90)
sarah.forward(50)
sarah.left(90)
sarah.forward(50)
sarah.left(90)
sarah.forward(50)
sarah.left(90)

canvas.exitonclick()
