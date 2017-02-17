import turtle
wn=turtle.Screen()
alex=turtle.Turtle()

st = []

def func_X(size,lvl):      #Function for X first variable
	if lvl < 1:
		alex.forward(size)
	else:
		func_F(size,lvl-1)
		alex.left(25)
		st.append([alex.xcor(),alex.ycor(),alex.heading()])
		st.append([alex.xcor(),alex.ycor(),alex.heading()])
		func_X(size,lvl-1)
		alex.penup()
		m = st.pop()
		i,j = m[0],m[1]
		alex.goto(i,j)
		alex.seth(m[2])
		alex.pendown()
		alex.right(25)
		func_X(size,lvl-1)
		alex.penup()
		m = st.pop()
		i,j = m[0],m[1]
		alex.goto(i,j)
		alex.seth(m[2])
		alex.pendown()
		alex.right(25)
		func_F(size,lvl-1)
		st.append([alex.xcor(),alex.ycor(),alex.heading()])
		alex.right(25)
		func_F(size,lvl-1)
		func_X(size,lvl-1)
		alex.penup()
		m = st.pop()
		i,j = m[0],m[1]
		alex.goto(i,j)
		alex.seth(m[2])
		alex.pendown()
		alex.left(25)
		func_X(size,lvl-1)
def func_F(size,lvl):      #Function for F first variable
	if lvl < 1:
		alex.forward(size)
	else:
		func_F(size,lvl-1)
		func_F(size,lvl-1)


if __name__=='__main__':
	alex.left(90)
	func_X(int(input()),int(input()))
	wn.exitonclick()