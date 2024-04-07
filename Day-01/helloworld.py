print("Hello World")

# Operations on operands
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(3%4)
print(3**4)
print(3//4)

# Data Type checking for the data

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type("finland"))
print(type("India"))

# Different Data Types Examples

# 1. Number (Integer and  float)

print("Integer Number = ",10,type(10))
print("Float Number= ",5.7,type(5.7))
print("complex number = ",1-3j,type(1-3j))

# 2. String 

print("String = ","hello",type("hello"))

# Boolean

print("boolean = ", 3>5 , 4<5 , type(4<5))

# List

newlist = [1,"helloworld",3.14]
print("List = ",newlist)

# Tuple

newtuple = (1,2,3,4,5,6)
print("tuple=",newtuple)

# set

newset = {3.14, 7, 98}
print("set=",newset)

# Dictionary

newpair = {
    'name':'priya',
    'country':'india',
    'age':'22',
}
print("dictionary= ",newpair)

# Euclidian distance between (2,3) and (10,8)
# euclidian distance d(p,q)^2 = (q1 - p1)^2 + (q2-p2)^2

p1,q1,p2,q2 = 2,3,10,8
distance = (q1-p1)**2 + (q2-p2)**2
print(distance)