#Coding Starts

```python
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



```

