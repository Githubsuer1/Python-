# 1. Mutable data types are those data types that can be modified or changed after creation. 
# 2. Immutable data types are those that can't be altered or modified after creation.

# 3. In python, variables stores reference of value in memory rather then actual value.

# 4. Python have automatic garbage collector means if nobody is referencing a value in memory then python will free the memory by self.
# 5. Actually immutability means we can not modify the reference of a value in memory but can store the reference of another value.

x = 10  # storing the reference of 10

y = x   # y is also storing the reference of 10 by via x


print(f'x is {x} and y is {y}')     # output: 10 10 

x = 15  # x is storing the reference of 15

print(f'x is {x} and y is {y}')     # output: 15 10

# list object
myList = [1,2,3,4]

myList1 = myList    # myList1 is storing the reference of the given list object

myList[1] = "SiddhantM"     # modifying the value at specified index in given list object

print(id(myList))           # id:2381862031424
print(id(myList1))          # id:same as myList ie. "2381862031424"

print(myList)               # output: [1, 'SiddhantM', 3, 4]
print(myList1)              # output: [1, 'SiddhantM', 3, 4]