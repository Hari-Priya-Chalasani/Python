# Day- 3 : Exercise-01

age = 22 # 1. Declare your age as integer variable
height = 5.2 # 2. declare your height as a  float variable
comple_Num = 1+3j # 3. Declare a variable that store a complex number

# 4. write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle  (area = 0.5 * b* h)

base = int(input("Enter the base of a triangle: "))
height = int(input("Enter the height of the triangle: "))

area = int(0.5 * base * height)

print("The area of the triangle is",area)

# 5. write a script that prompts the user to enter side a  and side b and side c of the triangle and calculate the perimeter of this triangle  (perimeter = a+b+c)

a = int(input("Enter side a of the triangle: "))
b = int(input("Enter side b of the triangle: "))
c = int(input("Enter side c of the triangle: "))

perimeter = a + b + c

print("The perimeter of the triangle is",perimeter)

# 6. Calculate area and perimeter  of a rectangle by taking the length and width as inputs  (area = l*w) (perimeter = 2* (l+w))

length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("the area of the rectangle is",area,",the perimeter of the rectangle is",perimeter)

# 7. Calculate area and circumstances of the circle by taking the user imputs. (area = pi * r*r) (circumstance = 2 * pi *r) (pi = 3.14)

radius = int(input("Enter the radius of the circle: "))
pi = 3.14

area = pi * (radius ** 2)
circumstance = 2 * pi * radius

print("the area of the circle is",area,", the circumstance of the circle is",circumstance)

#  8. Calculate the slope, x-intercept and y-intercept of y = 2x-2

x = int(input("Enter the x value: "))
y = int(input("Enter the y value: "))

x_intercept = 2 * y - 2
y_intercept = 2 * x - 2

slope_1 = y_intercept / x_intercept 

print("the slope is: ",slope_1)

#find the length of the 'python' and 'dragon' and make falsy comparision statement.

print(len('python')==len('dragon'))

# use and operator to check if 'on' is found in both 'python' and 'dragon'

if ('on' in 'python') and ('on' in 'dragon'):
    print("yes there is on in both python and dragon")

# there is no 'on' in both dragon and python

is_there = ('on' in 'python') and ('on' in 'dragon')
print(is_there)

# find the length of the word python and convert the value to float and convert it to string

length = len('python')

length = float(length)
length = str(length)

print(type(length))

# check if type of '10' is equal to type of 10

print(type('10')==type(10))

# check if int('9.8') is equal to 10

print('9.8' == 10) 

# check if floor division of 7 with 3 is equal to the int converted value of 2.7

floor = int(7//3)

print(floor == 2.7)

# find the number wheter it's even or odd

number = int(input("enter the number: "))

if number % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# 

n = 6

for i in range(1,n):
    print(i,"1",i,i**2,i**3)