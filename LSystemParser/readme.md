#L-Systems
An L-system or Lindenmayer system is a parallel rewriting system and a type of formal grammar. The recursive nature of the L-system rules 
leads to self-similarity and thereby, fractal-like forms are easy to describe with an L-system.

###Examples of L-systems:
 + (A → ABA), (B → BBB) - Cantor Set
 + (F → F+F−F−F+F) - Koch Curve

###File List
 + test1.py -- L system generator program
 + generated_new_python_file -- Generated file by test1.py<br/>

###Usage
Input should be [variables 1 2 ... n],degree,[L-rule 1;2;...;n]

First variable become the starting function.
For below below L-system, input for [test1.py](./LSystemParser/test1.py) should be:- <br/>
``` Console
D:/> test1.py
generated_new_python_file                          -- New python file having the generated version of the L-system
X F,25,X->F-[[X]+X]+F[+FX]−X;F->FF                 -- Variables, degree and Rule

```

###L-system complete data
variables : X F<br/>
constants : + − [ ]<br/>
start  : X<br/>
rules  : (X → F−[[X]+X]+F[+FX]−X), (F → FF)<br/>
angle  : 25°<br/>

The output of test1.py will be a [new python file](./LSystemParser/generated_new_python_file.py) with self generated program based on the rule.<br/>
For the new file, always the first input will refer the value for move forward and the next input will be the recursive level.<br/>

```Console
D:/> generated_new_python_file.py
5
6
```
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FOR REFERENCE](https://en.wikipedia.org/wiki/L-system)
