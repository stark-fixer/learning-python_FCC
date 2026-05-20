#IS and IN
#is
light_switch=True
if light_switch is 1: #now here it will not return anything, since the 'is' operator treats 1 as a number and True.
    print('Switch off the light!')
#instead of this, we can use the following code:
light__switch=True#or 1
if light_switch:
    print('ON')

#in
just_a_str='hello world!'
if 'hello' in just_a_str: #cheking whether the string is in the given value just_a_str='hello world!'.
    print('booyah!, found the word.') 

#TERNARY OPERATOR:
#CASE1
def age_adult(age):
    if age>18:
        return 'ADULT'
    else:
        return 'Adolescence'

#CASE2
def age_adult(age):
    return 'ADULT' if age > 18 else 'Adolescence' #just written if-else statement in one line, avoiding the dual use of the return statement


#STRINGS:
name='tommy'#str1
s_name='pandey'#str2
print(name+s_name)#concatinating strings or just adding strings using the + operators

#multiline string:
print("""I 
am
the
game
""") #it will print each and every string in an extra line


#STRING METHODS:
print('tommy'.upper())#TOMMY
print('toMMy'.lower())#tommy
print('stark fixer'.title())#Stark Fixer
print('stark Fixer'.islower())#False  

#types of string methods:

name = "stark fixer"
# Check if all characters are letters (False because of the space)
print(name.isalpha())  # Output: False

# Check if all characters are lowercase
print(name.islower())  # Output: True

# Check if the string contains only spaces
print(name.isspace())  # Output: False

name = "stark fixer"
# Split the string into a list of words based on spaces
print(name.split())  # Output: ['stark', 'fixer']

# Join elements together using 'stark fixer' as the glue
print(name.join(["1", "2"]))  # Output: 1stark fixer2

name = "stark fixer"
# Replace a word or character with something else
print(name.replace("fixer", "tony"))  # Output: stark tony

# Strip spaces from both sides (example includes extra spaces)
dirty_name = "  stark fixer  "
print(dirty_name.strip())  # Output: stark fixer

name = "stark fixer"
# Count how many times a character appears
print(name.count("r"))    # Output: 2

# Find the position (index) of the first match
print(name.find("fix"))   # Output: 6

# Check if the string starts with a specific word
print(name.startswith("stark"))  # Output: True

# Check if the string ends with a specific word
print(name.endswith("fixer"))    # Output: True

name = "stark fixer"
# Capitalise the very first letter
print(name.capitalize())  # Output: Stark fixer

# Capitalise the first letter of every word
print(name.title())       # Output: Stark Fixer

# Convert all letters to uppercase
print(name.upper())       # Output: STARK FIXER

# Convert all letters to lowercase
print(name.lower())       # Output: stark fixer

# Swap uppercase to lowercase and vice versa
print("StArK FiXeR".swapcase())  # Output: sTaRk fIxEr


#ESCAPING CHARACTERS:
name='tommy'
#now, let's say I have to add a ' in between two 'm' in tommy, then I CAN'T do that like this: print('tom'my')
#for this, I can either use \ or I can use "" strings to put a ' in between
name='tom\'my'
print(name)#tom'my
name="tom'my"
print(name)#tom'my
#"\" is the escape character


#STRING CHARACTERS AND SLICING:
#example;
name='stark'
print(name[2])#a
print(name[0])#s
print(name[1:2])#all characters starting at index 1 and ending before index 2 i.e. t
print(name[1:3])#ta
print(name[:4])#return everything upto character 4 i.e. star
print(name[:])#return all the characters from first to last i.e. stark

#BOOLEANS:
#these are basically true and false value
done = True #a type of boolean value except False
if done:
    print('yes')
else:#for false
    print('no')

print(0 == False)#True, since 0 is Considered False except all the integers
my_dict={}
print(bool(my_dict))#False, an empty dictionary is false in boolean

#THE 'ANY()' FUNCTION:
#basically the any() function returns if any of the value passed in it is true or not.
names=['stark',0,'naman',False]
print(any(names))#True
#but, it will only check iterable values, like list, string, dictionary...but not non-iterable like integer
#print(any(234));type error: non-iterable quantity
print(any('stark'))#True

#THE 'ALL' FUNCTION:
#basically the 'all' function returns True when all of the values are True within it. 
print(all(['stark',True]))#True
#print(all(["stark",False,0]))#False;since all values are not true
