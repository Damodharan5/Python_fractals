# The Sierpinski Triangle

It is a fractal and attractive fixed set with the overall shape of an equilateral triangle, subdivided recursively into smaller equilateral triangles. 

1. Start with an equilateral triangle.
2. Subdivide it into four smaller congruent equilateral triangles and remove the central one.
3. Repeat step 2 with each of the remaining smaller triangles

Recursive three line coding
----------------------------

``` python

treee(x1,y1,(x1+x2)/2,(y1+y2)/2,(x3+x1)/2,(y3+y1)/2,len/2,min)
treee(x2,y2,(x2+x3)/2,(y2+y3)/2,(x1+x2)/2,(y1+y2)/2,len/2,min)
treee(x3,y3,(x2+x3)/2,(y2+y3)/2,(x3+x1)/2,(y3+y1)/2,len/2,min)

```

![The Sierpinski Triangle](/triangle.png) "Screenshot for the fractals"
