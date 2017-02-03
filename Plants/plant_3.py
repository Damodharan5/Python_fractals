# http://python3.codes/drawing-fractals-with-lindenmayer-systems/ - For stack operations
# https://en.wikipedia.org/wiki/L-system - L system algorithms

import turtle

wn = turtle.Screen()
st = []
alex = turtle.Turtle()
alex.speed(0)

def ff(size,lvl):
	if lvl < 1:
		alex.forward(size)
	else:
		ff(size,lvl - 1)
		ff(size,lvl - 1)

def plant(size,lvl):
	if lvl >= 1:
		ff(size,lvl - 1)
		alex.right(25.7)
		st.append([alex.xcor(),alex.ycor(),alex.heading()])
		st.append([alex.xcor(),alex.ycor(),alex.heading()])
		plant(size,lvl - 1)
		alex.penup()
		m = st.pop()
		i,j = m[0],m[1]
		alex.goto(i,j)
		alex.seth(m[2])
		alex.pendown()
		alex.left(25.7)
		plant(size,lvl-1)
		alex.penup()
		m = st.pop()
		i,j = m[0],m[1]
		alex.goto(i,j)
		alex.seth(m[2])
		alex.pendown()
		alex.left(25.7)
		ff(size,lvl - 1)
		st.append([alex.xcor(),alex.ycor(),alex.heading()])
		alex.left(25.7)
		ff(size,lvl-1)
		plant(size,lvl - 1)
		alex.penup()
		m = st.pop()
		i,j = m[0],m[1]
		alex.goto(i,j)
		alex.seth(m[2])
		alex.pendown()
		alex.right(25.7)
		plant(size,lvl-1)

if __name__ == '__main__':
	alex.left(90)
	alex.penup()
	alex.goto(-200,-200)
	alex.pendown()
#	alex.width(1)
	plant(int(input("Enter the Size: ")), int(input("Enter the depth: ")))
	print("Finished Processing....!")
	alex.hideturtle()
	wn.exitonclick()
