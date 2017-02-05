##############################################################################################################################################
#Creating a program which accepts the L-system rule and convert it into a .py file                                                           #
#2/5/2017 - Creating a function which parse the L-rule                                                                                       #
#So far accomplished the parsing of all except the '[' , ']' - stack operations for push and pop the current location                        #
##############################################################################################################################################
import os
fp = ""
def __Linit__():
	fp.write("import turtle\nwn=turtle.Screen()\nalex=turtle.Turtle()\n\n")#expecting more lines below

def __Lfinal__(arg1):
	fp.write("\n\nif __name__=='__main__':\n\t"+arg1+"(int(input()),int(input()))\n\twn.exitonclick()")

def Lparse(a): # Input should be [variables 1],degree,[L-rule 1] ....[L-rule n]
	dic = {}
	lis_sp = a.split(',')        # Spilt the input command.
	overall_func = lis_sp[0].split(" ")
	# for to create a dic of func calling. later used in writing file
	for i in overall_func:
		dic[i] = 'func_'+i+'(size,lvl-1)'
	dic['-'] = 'alex.left('+lis_sp[1]+')'
	dic['+'] = 'alex.right('+lis_sp[1]+')'	
	print(dic)
	magic = lis_sp[2].split(';')   # Rules splitted
	print(magic)
	for ind,i in enumerate(overall_func):
		fp.write("def func_"+i+"(size,lvl):      #Function for "+i+" first variable\n\tif lvl < 1:\n\t\talex.forward(size)\n\telse:\n")
		for i in magic[ind].split('->')[1]:
			fp.write('\t\t'+dic[i]+'\n')
	__Lfinal__("func_"+overall_func[0])		

if __name__ == '__main__':
		fp = open(input()+".py","w")
		__Linit__()
		Lparse(input())
		fp.close()
