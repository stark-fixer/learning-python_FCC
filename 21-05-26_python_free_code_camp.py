#USER INPUTS:
#for example
#print('what\'s your favourite subject? ')
#fav_subject = input()
#print('your favourite subject is: '+fav_subject)
#you can also do the same thing in this way:
#fav_subject  = input('what\'s your favourite subject? ')
#print('your favourite subject is: ',fav_subject)


#CONTROL STATEMENT:
condition = True
if condition == True:
    print('the condition')
    print('is true')
else:
    print('the condition')
    print('is false')


#LISTS:
my_list = ['tommy',1,True,1.2,'fixer','Tom',False]
print(my_list[0])#'tommy'
print(my_list)#['tommy',1,True,1.2,'fixer']
my_list[3]=3.14
print(my_list)#['tommy',1,True,3.14,'fixer']
print(my_list[2:4])
print(len(my_list))#7
my_list.append("Sana")#it will add the string 'Sana' to the list
print(my_list)#['tommy', 1, True, 3.14, 'fixer', 'Tom', False, 'Sana']
my_list.extend(['Sana','Chandresh'])#now here, you can add more than 1 item in the existing list
print(my_list)#['tommy', 1, True, 3.14, 'fixer', 'Tom', False, 'Sana', 'Sana', 'Chandresh']
my_list += ['Sana','Chandresh']#same thing as "my_list.extend(['Sana','Chandresh'])"
print(my_list.pop()) #remove the last item from the list i.e. Chandresh
print(my_list)#['tommy', 1, True, 3.14, 'fixer', 'Tom', False, 'Sana', 'Sana', 'Chandresh', 'Sana']
my_list += ['Chandresh']

list2=['tommy',1,True]
list2.insert(2, False)#['tommy', 1, False, True]
print(list2)
list2[1:2]=['stark','fixer']
print(list2)#['tommy', 'stark', 'fixer', False, True]


#SORTING LIST:
list3=['tommy','stark','sam','beau','Tom']
list3copy=list3[:] #this will make sure that the list is in the same order
list3.sort()#will sort the list items in alphabetical order
print(list3)#['Tom', 'beau', 'sam', 'stark', 'tommy']
list3.sort(key=str.lower)#it doesn't care about the uppercase or lower case letter
print(list3)#['beau', 'sam', 'stark', 'Tom', 'tommy']
#the way to sort the list without modifying the original list:
print(sorted(list3,key=str.lower))#it will only print the sorted list, but won't change the list

print(list3)
print(list3copy)#the original list i.e.['tommy', 'stark', 'sam', 'beau', 'Tom']
