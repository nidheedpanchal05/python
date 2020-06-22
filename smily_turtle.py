#Draw a smily 
#using turtle module in python

#import turtle module
import turtle 
#import the time module
import time

turtle.bgcolor('black')
#create pen
p = turtle.Pen()
#set width of pen
p.width(5)
#hide the turtle
p.hideturtle()
#change the color of pen as yellow
p.color('yellow')
#------------to draw circle/body-------------
#put the pen down
p.down()
#rotate turtle 180 to left
#to draw circle top to bottom
p.left(180)
p.circle(100)
#pick the pen up
p.up()
#------to bring the turtle towards eye------
#rotate turtle 90 to left
#bring turtle down i.e forward 80
p.left(90)
p.forward(80)
#again turn the turtle left 90
#move straight left i.e fwd 30
p.left(90)
p.forward(30)
#--------to draw eyes of our smily--------
p.down()
#draw circle of radius 20 i.e 1st eye
p.circle(20)
#pen up
p.up()
#move the turtle to equal distance
#from the 1st eye
p.right(180)
p.forward(60)
p.right(180)
#pen down
p.down()
#draw the 2nd eye
p.circle(20)
p.up()
#---------to move turtle to the smile--------
#rotate 50 towards right
#go down i.e forward 50
p.right(90)
p.forward(50)
p.left(90)
#move turtle backwards to get big smile
p.backward(20)
p.right(70)
#----------to make a smile--------
p.down()
#a smile is nothing but an arc
#create an arc using for loop
for i in range(6,17):
	p.left(12)
	p.forward(12)
p.up()
#to stop the execution for 2 sec
time.sleep(2)