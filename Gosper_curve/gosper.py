# Gosper Curve
# https://en.wikipedia.org/wiki/Gosper_curve

import turtle

wn = turtle.Screen()

alex = turtle.Turtle()

def A(size,lvl):
	if lvl < 1:
		alex.forward(size)
	else:
		A(size,lvl-1)
		alex.right(60)
		B(size,lvl-1)
		alex.right(120)
		B(size,lvl-1)
		alex.left(60)
		A(size,lvl-1)
		alex.left(120)
		A(size,lvl-1)
		A(size,lvl-1)
		alex.left(60)
		B(size,lvl-1)
		alex.right(60)

def B(size,lvl):
	if lvl < 1:
		alex.forward(size)
	else:
		alex.left(60)
		A(size,lvl-1)
		alex.right(60)
		B(size,lvl-1)
		B(size,lvl-1)
		alex.right(120)
		B(size,lvl-1)
		alex.right(60)
		A(size,lvl-1)
		alex.left(120)
		A(size,lvl-1)
		alex.left(60)
		B(size,lvl-1)

	



if __name__ == "__main__":
	alex.speed(int(input("Enter the speed: ")))
	alex.left(90)
	A(int(input("Enter the size: ")),int(input("Enter the lvl: ")))
	print("Finished Processing...!")
	alex.hideturtle()
	wn.exitonclick()
