#Coding Starts
# The Sierpinski Triangle

import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

def line(x1,y1,x2,y2):
	alex.penup()
	alex.goto(x1,y1)
	alex.pendown()
	alex.goto(x2,y2)
	
def eqtr(x1,y1,x2,y2,x3,y3):
	line(x1,y1,x2,y2)
	line(x3,y3,x2,y2)
	line(x1,y1,x3,y3)   

def treee(x1,y1,x2,y2,x3,y3,len,min):
	eqtr((x1+x2)/2,(y1+y2)/2,(x2+x3)/2,(y2+y3)/2,(x3+x1)/2,(y3+y1)/2)
	if(len >= min):
		treee(x1,y1,(x1+x2)/2,(y1+y2)/2,(x3+x1)/2,(y3+y1)/2,len/2,min)
		treee(x2,y2,(x2+x3)/2,(y2+y3)/2,(x1+x2)/2,(y1+y2)/2,len/2,min)
		treee(x3,y3,(x2+x3)/2,(y2+y3)/2,(x3+x1)/2,(y3+y1)/2,len/2,min)
		
if __name__ == "__main__":
	len=input("Enter the side: ")
	eqtr(len/2,-1.732*len/6,-len/2,-1.732*len/6,0,len/1.732)
	treee(len/2,-1.732*len/6,-len/2,-1.732*len/6,0,len/1.732,len,input("Enter the min size: "))   # The Sierpinski Triangle
	alex.hideturtle()
	wn.exitonclick()
