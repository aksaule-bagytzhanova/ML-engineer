# a = 2 + 2
# b = a + 4
# print(a, b)

#######3
# a = 17 / 3 #returns float
# print(a)

# a = 17 // 3 #returns integer 
# print(a)

# a = 17 % 3 #returns remainder of the division
# print(a) 

# a = 17 ** 3 #17 to the power of 3
# print(a)

# tax = 12.5 / 100 
# price = 100.50 
# print(price * tax)
# print("1" + _)

# a = "sams eggs"
# a = 'sams eggs'

# a = "I want to escape this \'"
# print(a)

# a = 'And I may escape this by that " '
# print(a)

a = 'And I may do it. \nTomorrow I will be happy'
print(a)

a = r"If you don't want characters prefaced by \ do r before quote"
print(a)

a = "do po 3 times "
print(a*3)

a = "a" * 3 + "b" #we can do this
print(a)

a = "a"  "b" # will be connected
print(a)

a = "We can indexing strings" #positive indexies start by 0, negitive with -1
print(a[4])

a = "apple" #we have slicing
print(a[0:3])

a = "Python"
print(a[:2], a[4:]) #from beginning [:4], and from number till the end [1:]

#strings can not be change 

a = len("rojrjoihobfd'bf'ln'bkfnfb") #length
print(a)

#####Lists 
a = ["apple", "orange", "list", 4, 4, 1]
print(a)

a = a[1] #also will be indexed
print(a)

a = ["apple", "orange", "list", 4, 4, 1] #Lists also support operations like concatenation
print(a+a)

a = ["apple", "orange", "list", 4, 4, 1] #adding elements
a.append("opopopo")
print(a)

"""Простое присвоение в Python никогда не приводит к 
копированию данных. Когда вы присваиваете список переменной, 
переменная ссылается на существующий список. Любые изменения,
которые вы вносите в список с помощью одной переменной, будут 
видны через все другие переменные, которые ссылаются на нее.:"""

a = ["rt", 3]
b = a
print(a, b) #['rt', 3] ['rt', 3]
a.append("4")
print(a, b) #['rt', 3, '4'] ['rt', 3, '4']


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
print(letters) #['a', 'b', 'C', 'D', 'E', 'f', 'g']

# now remove them
letters[2:5] = []
print(letters) #['a', 'b', 'f', 'g']

letters[:] = []
print(letters) #empty list

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] #we have method to find length to list
print(len(letters))

#Also have nest list 
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)