'''
Isabel Hartley
03 Nov 2024
P4LAB1
Writing a turtle graphics program that draws a triangle and a square.
'''

import turtle

t = turtle.Turtle()
t.speed(1) 
for _ in range(4):
    t.forward(100)  
    t.right(90)    

t.penup()          
t.goto(-50, -50)
t.pendown()       

for _ in range(3):
    t.forward(100)  
    t.left(120)     

turtle.done()
