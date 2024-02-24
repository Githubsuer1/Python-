# Data types used to specify the type of data stored inside the variable. 
# In python, data types also known as object types. 

# 1. Number data type contains different types of numbers like integer, floating point, complex etc.

number1 = 1234
print(type(number1))        # <class 'int'>

number2 = 3.14
print(type(number2))        # <class 'float'>

number3 = 3+4j
print(type(number3))        # <class 'complex'>


# 2. Strings data type contains array of charectors, written in single or double quoats

str1 = "python"
str2 = "javaScript"

print(type(str1))       # <class 'str'>
print(type(str2))       # <class 'str'>

# 3. List is a class,also called dynamic array, ordered, indexed, heterogeneous data type, braces is used

myList1 = [1,2,3,"python", "java",["c","c++",1,2,3],(1,2,3),list(range(10))]

print(type(myList1))        # <class 'list'>
print(myList1)              # [1, 2, 3, 'python', 'java', ['c', 'c++', 1, 2, 3], (1, 2, 3), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]

# 4. Tuple is class, different from list, ordered, indexed, immutable, paranthesis is used, immutable

myTuple1 = (1,2,3,"tuple","string",3.14,(2,3,56))

print(type(myTuple1))           # <class 'tuple'>
print(myTuple1)                 # (1, 2, 3, 'tuple', 'string', 3.14, (2, 3, 56))


# 5. Dictionary is a class, key value pair used to store data, key should be unique, ordered, indexed, mutable

myDict1 = {'name':'chai','flavour':'masala','price':125} 

print(type(myDict1))           # <class 'dict'>
print(myDict1)                 # {'name': 'chai', 'flavour': 'masala', 'price': 125}


# 6. Set is a class, should be unique, unordered, unindexed, mutable

mySet1 = {1,2,3,4,5,6}

print(type(mySet1))         # <class 'set'>
print(mySet1)               # {1, 2, 3, 4, 5, 6}

# 7. File: open('eggs.txt'), open(r'C:\ham.bin','wb')

# 8. Boolean: True or False 

# 9. None : None 

# 10. Functions, modules, classes

# 11. Advance : Decorators, Iterators, Generators, MetaProgramming

