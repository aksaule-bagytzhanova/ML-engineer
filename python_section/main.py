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

# a = 'And I may do it. \nTomorrow I will be happy'
# print(a)

# a = r"If you don't want characters prefaced by \ do r before quote"
# print(a)

# a = "do po 3 times "
# print(a*3)

# a = "a" * 3 + "b" #we can do this
# print(a)

# a = "a"  "b" # will be connected
# print(a)

# a = "We can indexing strings" #positive indexies start by 0, negitive with -1
# print(a[4])

# a = "apple" #we have slicing
# print(a[0:3])

# a = "Python"
# print(a[:2], a[4:]) #from beginning [:4], and from number till the end [1:]

# #strings can not be change 

# a = len("rojrjoihobfd'bf'ln'bkfnfb") #length
# print(a)

# #####Lists 
# a = ["apple", "orange", "list", 4, 4, 1]
# print(a)

# a = a[1] #also will be indexed
# print(a)

# a = ["apple", "orange", "list", 4, 4, 1] #Lists also support operations like concatenation
# print(a+a)

# a = ["apple", "orange", "list", 4, 4, 1] #adding elements
# a.append("opopopo")
# print(a)

# """Простое присвоение в Python никогда не приводит к 
# копированию данных. Когда вы присваиваете список переменной, 
# переменная ссылается на существующий список. Любые изменения,
# которые вы вносите в список с помощью одной переменной, будут 
# видны через все другие переменные, которые ссылаются на нее.:"""

# a = ["rt", 3]
# b = a
# print(a, b) #['rt', 3] ['rt', 3]
# a.append("4")
# print(a, b) #['rt', 3, '4'] ['rt', 3, '4']


# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters[2:5] = ['C', 'D', 'E']
# print(letters) #['a', 'b', 'C', 'D', 'E', 'f', 'g']

# # now remove them
# letters[2:5] = []
# print(letters) #['a', 'b', 'f', 'g']

# letters[:] = []
# print(letters) #empty list

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] #we have method to find length to list
# print(len(letters))

# #Also have nest list 
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)


###############################4444444444444444444

# x = int(input("Please enter the number: "))

# if x == 0:
#     print('This number 0')  
# elif x > 1 and x < 8:
#     print('This number from 1 to 8')
# else: 
#     print("Hope that this is number")

####4,2
# words = ["apple", 'pineapple', 'yoyo']

# for w in words:
#     print(w, len(w))

"""
apple 5
pineapple 9
yoyo 4
"""
import pickle


# users = {"Sula" : "inactive", "Aksaule" : "active", "Aruzhan" : "inactive"}
# print(users.items())
# print(type(users.items()))
# for user, status in users.copy().items():
#     print(user, status)
#     if status == 'inactive':
#         del users[user]
#
# active_users = {}
# print(users)
#
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
#
# print(users)
# print(active_users)

#
# for number in range(6):
#     print(number)
#
# a = list(range(4, 10, 2))
# print(a)
#
# a = list(range(-10, -100, -30))
# print(a)

#range and len()
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


#####break and continue
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break

# for num in range(2, 10):
#     if num % 2  == 0:
#         print(f"Found an even number {num}")
#         continue
#     print(f"Found an odd number {num}")

###############else Clauses on Loops
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break
#     else:
#         print(f"{n} is a prime number")

##################pass
# class MyEmptyClass:
#     pass

################match
# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 401 | 403:
#             return "Not allowed"
#         case _:
#             return "just ask Aksi what is it"
#
# print(http_error(403))

# class Point:
#     __match_args__ = ("x", "y")
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y point is {y}")
#         case Point(x=x, y=0):
#             print(f"X point is {x}")
#         case Point(x, y) if x == y:
#             print(f"X point equal Y point")
#         case Point():
#             print("Somewhere else")
#         case _:
#             print("Not a point")
#
# p1 = Point(4, 0)
# where_is(p1) #X point is 4
#
# p2 = Point(9, 6)
# where_is(p2) #Somewhere else
#
# p3 = Point(6, 6)
# where_is(p3) #X point equal Y point

##############match in list and tuple
# match [1, 2, 3]:
#     case x, y, z:
#         print(x, y, z)

# match [1, 2, 3, 4]:
#     case x, y, *_:
#         print(x, y)

#########def

####global
# x = 10
#
# def update_global():
#     global x
#     x = 20
#
# print(x)
# update_global()
# print(x)

######default arguments
# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         reply = input(prompt)
#         if reply in {'y', 'ye', 'yes'}:
#             return True
#         if reply in {'n', 'no', 'nop', 'nope'}:
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
#
# ask_ok('Do you really want to quit?')

# i = 5
#
# def f(arg=i):
#     print(arg)
#
# i = 6
# f() #output:5

# def f(a, L=[]):
#     L.append(a)
#     return L
#
# print(f(1)) #[1]
# print(f(2)) #[1, 2]

# def get_info(nation, name='Aksi', age='24'):
#     print(f"This her name {name}")
#     print(f"This is her {age}")
#     print(f"{name} nation is {nation}")
#
# get_info(nation='kaz', age="5")

# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

#output:
"""
-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
"""

# def position_only(name, /):
#     print('This is', name)
#
# position_only('Ths')
#
# def named_only(*, name):
#     print(f'This is name, {name}')
# named_only(name="ttoo")

# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)
#
# combined_example(1, standard=2, kwd_only=3)
# #output: 1 2 3

#unpacking
#list
# a = list(range(2, 8))
# print(a)
#
# args= [4, 9]
# a = list(range(*args))
# print(a)

#dict
# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
#
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

#lambda
# def make_incrementor(n):
#     return lambda x: x + n
#
# f = make_incrementor(40)
# print(f(8)) #output 48
#
# print(f(55)) #95

######5 List methods
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
#
# print("#######append#########")
# fruits.append('kiwi')
# print(fruits)
#
# print("#######extend########")
# fruits_2 = ['apple', 'pineapple']
# fruits.extend(fruits_2)
# print(fruits)
#
# print("#########insert########")
# fruits.insert(1, 'watermelon')
# print(fruits)
#
# print("#########remove#########")
# fruits.remove('apple')
# print(fruits)
#
# print("#########pop###########")
# f_item = fruits.pop(5)
# print(f_item)
# print(fruits)
#
# print("#########clear##########")
# fruits_2.clear()
# print(fruits_2)
#
# print("##########index##########")
# a = fruits.index('kiwi')
# print("index work of kiwi", a)
#
# print("##########count##########")
# r = fruits.count('kiwi')
# print(r)
#
# print("##########sort##########")
# numbers_list = [5, 7, 9, 4, 13, 65, 0, 6, 1]
# numbers_list.sort()
# print(numbers_list)
#
# print("##########reverse##########")
# numbers_list.reverse()
# print(numbers_list)
#
# print("##########copy##########")
# numbers_copy = numbers_list.copy()
# print(numbers_copy)

#####Stacks
# stack = [3, 4, 5]
#
# stack.append(9)
# stack.append(4)
# print(stack)
#
# stack.pop()
# print(stack)

#####Queue
# from collections import deque
#
# queue = deque(['Aksi', 'Sula', 'Elmira', 'Jankuat'])
#
# queue.append('Bakut')
# print(queue)
#
# queue.appendleft('Azamat')
# print(queue)
#
# queue.pop()
# print(queue)

########List Comprehensions
# a = list(map(lambda x: x**2, range(10)))
# ###or
# squares = [x**2 for x in range(10)]
# print(squares)

# from math import pi
# out = [str(round(pi, i)) for i in range(1, 6)]
# print(out)

#######Nested List Comprehensions
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# column_to_row = [[row[i] for row in matrix] for i in range(4)]
# print(column_to_row)
#
# print("this is # matrix", *matrix)
# print("this is just matrix", matrix)
#
# column_to_row_2 = list(zip(*matrix))
# print(column_to_row_2)


#####DEL
# numbers_list = [1, 2, 4, 6, 3, 5]
# del numbers_list[4]
# print(numbers_list)
#
# del numbers_list[:]
# print(numbers_list)


######Tuple
# this_is_tuple = 3, 6, 45
# print(this_is_tuple)
# print(this_is_tuple[1])
#
# nested_tuple = this_is_tuple, (90, 455, 1)
# print(nested_tuple)
#
# #tuples are immutable
#
# new_tuple = ()
# print(len(new_tuple))
# print(len(this_is_tuple))
#
# #unpacking
# n1, n2, n3 = this_is_tuple
# print(n1, n2, n3)


########Sets
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)
#
# print("apple" in basket) #True
#
# a = set('abracadabra')
# b = set('alacazam')
# print(a) #{'r', 'a', 'd', 'b', 'c'}
# print(b) #{'l', 'm', 'a', 'z', 'c'}
#
# print(a-b) #{'r', 'b', 'd'} letters in a but not in b
# print(a|b) #{'c', 'd', 'z', 'b', 'l', 'm', 'r', 'a'}
# print(a&b) #{'c', 'a'}
# print(a^b) #{'d', 'b', 'z', 'm', 'r', 'l'}

########Dictionary
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4055
# print(tel)
#
# print(tel['jack'])
#
# tel['deleted_item'] = 555
# print(tel)
# del tel[('deleted_item')]
# print(tel)
#
# new_dict = dict(sape=4139, guido=4127, jack=4098)
# print(new_dict)

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for i in knights.items():
#     print(i)
#
# print(knights.items())

# ########enumerate
# for index, value in enumerate(['tic', 'tac', 'toe']):
#     print(index, value)
#
#
# ########zip
# questions = ['name', 'age', 'educations']
# answers = ['Aksi', '24', 'SDU']
#
# print(list(zip(questions, answers))) #[('name', 'Aksi'), ('age', '24'), ('educations', 'SDU')]
#
#
# ###########reversed
# for i in reversed(range(1, 9)):
#     print(i)
#
#
# #########sorted
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)

# import fibo as f
#
# print('Importing function')
# f.fib(1000)
#
# print(f.__name__)
#
# from fibo import fib, fib2
# fib(100)
#
# from fibo import fib as fibonacci
# fibonacci(9000)

# import sys
#
# print(sys.path)

# import fibo, sys
#
# print('####################################')
# print(dir(fibo))
#
# print('####################################')
# print(dir(sys))
#
# import packages.pk1


######Chapter 7
# year = 2016
# event = 'Referendum'
#
# print(f"this is year {year}, this is event {event}")

# yes_votes = 42_572_654
# total_votes = 85_705_149
# percentage = yes_votes / total_votes
# print('{:-9} Yes votes {:2.2%}'.format(yes_votes, percentage))

#####str or repr
# s = "Hello world"
# print(str(s))
# print(repr(s))

####formated str
# import math
# print(f"This is pi value {math.pi:.3f}.")

# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print(f'{name:10} ==> {phone:10d}')

