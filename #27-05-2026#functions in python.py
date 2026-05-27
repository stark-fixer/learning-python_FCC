#FUNCTIONS
#for example:
def hello(): #this is a function named hello(), we have created it of our own
    print('hello tommy!')
hello()#hello tommy!
    
def hello(name): #I can also pass a parameter in this
    print("Hello " + name)
hello("Stark")
hello("Sana")        

#parameter v/s argument: 
#parameter: it is the values accepted by the function inside the function
#argument: these are the values that we pass in the function; there  can also be default arguments(we can set them)
#hello() #error, since we have not specified a defaut value 
def hello(name = "my friend"):
    print("Hello " + name)
hello("Chandresh!") #Hello Chandresh!
hello()#now, it will print the defalut value: Hello my friend  
#adding multiple parameters
def hello(name, age):
    print("Hello " + name + ", you are " + str(age) + " years old!")
hello("tommy", 17) # Hello tommy, you are 17 years old!

#there are some types, which don't show change out of the function, some of them are integers, booleans, float, etc., 
#for example:
def change(value):
    value = 2 
val = 1
change(val)
print(val)  #it won't return 2, since it is an integer type, and it doesn't change...
#except these types, any other value will change...for example:
def change(value):
    value["name"] = "SANA"
val = {"name" : "tommy"}
change(val)
print(val)# this will change value from tommy to SANA.....{'name': 'SANA'}

#introducing the "return" thing:
#the return is not necessarily change the function's output, it means that the function has come to an end:
def test():
    print("Thi line will print")
    return "OVER"
    print("This statement will never run")#since we have already used the return.  

#difference b/w return and print()
# function-1: 
def add_with_print(a,b):
    answer = a + b
    print(answer) #this only SHOWS the number on the screen.. 
#function-2:
def add_with_return(a,b):
    answer = a + b
    return answer #this HANDSOVER the number to the 'answer' variable 

#using both functions:
#testing print()
box1 = add_with_print(5,5) #Screen prints: 10
print("Inside box1: ",box1) #Screen prints: Inside box1: NONE (since it didn't saved the value)
#testing return:
box2 = add_with_return(5,5)
print("Inside box2:",box2) #Screen prints: Inside box2: 10 (since it saved the value)

#using function with conditional statement:
def hello(name):
    if not name:
        return "no name!"
    print(f"Hello {name}") #it doesn't even need an else. 
hello(False) #no name! 
hello("Sana") #Hello Sana  

#returning multiple values in a function
def hello(name):
    print('Hello ' + name + '!')
    return name  + " Sharma " + " is " + " topper"

print(hello("Chandresh"))    


