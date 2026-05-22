#TUPLES
names = ('tommy','sana','stark','harry')
print(names[0])#tommy
print(names[-1])#harry
print(names.index('sana'))#1
print('stark' in names)#True
#creating a new tuple from an existing tuple
new_tuple = names + ('Chandresh','Utkarsh')
print(new_tuple)#('tommy', 'sana', 'stark', 'harry', 'Chandresh', 'Utkarsh')


#DICTIONARIES(are inmutable)
info = {'name':'tommy', 'age':17, 'fav_subject':'Physics'}
print(info['name'])#tommy
print(info.get('name'))#tommy
#setting a default value for an unknown key:
print(info.get('ikigai','coding'))#coading; in the 'info' dictionary, there is no key named ikigai, but lets say I want a default answer, for a key, if it is not in the dictionary, I can use the get()function there too
new_info={'name':'tommy', 'age':17, 'fav_subject':'Physics', 'ikigai':'coding'}
print(new_info.get('ikigai','drawing'))#coding
print(new_info.pop('ikigai'))# {'name':'tommy', 'age':17, 'fav_subject':'Physics'}
print(info.popitem())#it will remove and give the last key-value pair in the dictionary
print(info)#{'name':'tommy', 'age':17}
info = {'name':'tommy', 'age':17, 'fav_subject':'Physics'}
print('fav_subject' in info)#True
print(info.keys())#it will return all the keys in form of a list; dict_keys(['name', 'age', 'fav_subject'])
print(list(info.keys()))#it will now not print the dict_keys part, and will only return the list
info['ikigai']='coding' #adding a new key-value pair to the dictionary
print(info)#{'name': 'tommy', 'age': 17, 'fav_subject': 'Physics', 'ikigai': 'coding'}
del info['ikigai']#deleting a key-value pair from the dictionary
info_copy=info.copy()#copying the dictionary into a new dictionary
print(info_copy)#info


#SETS:(mutable, not ordered)
set1={'tommy','stark'}
set2={'stark'}
set3={'sana'}
intersect = set1 & set2 #will get the common element from the above two sets
print(intersect)#{'stark'}
union = set1 | set3#will get the union of the two sets
print(union)
print(list(set1))#will convert the set1 to a list
mod = set1-set2#will get the value {'tommy'}
mod_ = set1 < set2#will compare two sets
print(mod)#{'tommy'}
print(mod_)#False
