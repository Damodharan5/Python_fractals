#Fractal plant - Type 3

The recursive nature of the L-system rules leads to self-similarity and thereby, fractal-like forms are easy to describe with an L-system.

L-system rule
-----------------
<b>(X → F−[[X]+X]+F[+FX]−X), (F → FF)</b>

+ F - draw forward
+ - - turn right with some angle(25.7)
+ + - turn left with angle(25.7)
+ [ - push the current location and angle
+ ] - pop the stack

### Output
![](https://github.com/Damodharan5/Python_fractals/blob/master/Plants/plant3.PNG?raw=True)


