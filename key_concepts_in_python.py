#1.to run multiline code in one line, use ";"
name='tommy';print(name)
#2.You can also know which datatype your variable belongs to, for ex:
print(type(name))
#you can also check, whether your variable type is of the type you mentioned, for ex:
print(type(name)==int)
#you can also do the same thing(print(type(name)==int)) from the 'isinstance (obj,class type)' command, for example:
print(isinstance(name,str))
#you can also concatinate strings(means join 2 strings with +), for example:
print('Roman reings' + ' is the original big dog')

#HERE ARE ARITHEMATIC OPERATORS(NOW HERE i AM ONLY CONSIDERING THE ONES WHICH i WANT TO LEARN, NOT +,-,*.%,ETC.), FOR EXAMPLE
age=6
age+=6 #age=age+6
print(age) #it will print age=age+6 i.e. age=6+6 that is age=12

#BOOLIAN OPERATORS
roman_reings_OTC=1 #True
roman_reings_BIG_DOG=0 #False
print(not roman_reings_OTC) #False
print(roman_reings_OTC and roman_reings_BIG_DOG) #False
print(roman_reings_OTC or roman_reings_BIG_DOG) #True

#SPECIAL CASE OF 'OR': While using the 'or' with two operands, it returns the first operands until and unless it is false, if the first operand is false, then it returns the last operand
print(0 or 1) #1
print('hey' or 'hi') #'hey'
print(False or 'tommy') #'tommy'
print('[]'or False) #'[]'
print(False or '[]') #'[]'

#SPECIAL CASE OF 'AND': If the first value is false, AND returns it, and if it is true, it checks the other value and returns the output:
print(0 and 1) #0
print('hey' and 'hi') #'hi'
print(False and 'tommy') #False
print('[]'and False) #False
print([] and False) #[]

#HOW PYTON DOCS DESCRIBES AND and OR:
#for And[#the following code is as same as 'x AND y' with the following x and y values]
x=input('enter your input from True/False:') #taking the True or false input from user.
y='tommy' #a fixed input
if x=='False':
    print(x)
else:
    print(True)     

#for Or[the following code is as same as 'x or y' with following x and y values]
x=input('enter your input from these choise: True/False:')
y=input('enter your input from these choise: True/False:')
if x=='False':
    if y=='False':
        print(False)
    else:
        print(True)
if x=='True':
    print(y)                
