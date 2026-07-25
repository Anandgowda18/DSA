dict1 = {'value':11}
dict2 = dict1

print("Before the update of dict2 value:")
print("dict1=",dict1) #output dict1= {'value': 11}
print("dict2=",dict2) #output dict2= {'value': 11}
print("dict1 points to:",id(dict1)) #output The id of dict1 and dict2 will be same
print("dict2 points to:",id(dict2))

dict2['value'] = 22

print("After the update of dict2 value:")
print("dict1=",dict1) #output dict1= {'value': 22}
print("dict2=",dict2) #output dict2= {'value': 22}
print("dict1 points to:",id(dict1)) #output The id of dict1 and dict2 will be same, this is due to mutable
print("dict2 points to:",id(dict2))

#dictionary is mutable, so whenever you allocate a new value to a new variable. The old and the new variable still point to same id
