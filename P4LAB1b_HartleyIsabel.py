'''
Isabel Hartley
03 Nov 2024
P4LAB1
using tuetle graphics to create my initails
'''
import turtle


t = turtle.Turtle()
t.speed(1)  
t.pensize(5)  
t.color("blue")  

t.penup()
t.goto(-50, 0)  
t.pendown()


t.forward(50)  
t.penup()
t.goto(-50, 0)  
t.pendown()
t.backward(50)  


t.penup()
t.goto(-70, 0)  
t.pendown()
t.forward(40)   
t.penup()
t.goto(-70, -50) 
t.pendown()
t.forward(40)   


t.penup()
t.goto(30, 0)  
t.pendown()


t.forward(50)   
t.right(180)    
t.forward(50)   
t.right(90)
t.forward(30)   
t.right(90)
t.forward(50)   


t.penup()
t.goto(30, -25)  
t.pendown()
t.forward(30)   


t.penup()
turtle.done()
