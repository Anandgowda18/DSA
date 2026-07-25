num1 = 11
num2 = num1

print("Before update of num2:")
print("num1=",num1) #output will be 11
print("num2=",num2) #output will be 11
print("num1 points to:",id(num1)) # The id of num1 and num2 will be same
print("num2 points to:",id(num2))

num2 = 22

print("After update of num2:")
print("num1=",num1) #output will be 11
print("num2=",num2) #output will be 22
print("num1 points to:",id(num1)) #The id of nume and num2 will be different, this is because integers are immutable
print("num2 points to:",id(num2))

#integers are immutable, so whenever you allocate a new value to a new variable. The variable will take the new number
