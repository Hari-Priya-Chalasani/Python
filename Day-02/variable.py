# Day- 2 : Exercise-01

# Day2: 30 Days of Python

firstName = "Hari Priya" #Declare a first name variable and assign a value to it

lastName = "Chalasani" #Declare a last name variable and assign a value to it

fullName = "Hari Priya Chalasani"#Declare a full name variable and assign a value to it

country = "India" #Declare a country variable and assign a value to it

city = "Vijayawada" #Declare a city variable and assign a value to it 

age = 22 #declare a age variable and assign a value to it

year = 2024 #declare a year variable and assign a value to it

is_married = False #declare a variable is_married and assign a value to it

is_true = True #declare a variable is_true and assign a value to it 

is_light_on = True #declare a variable is_light_on and assign a value to it 

a,b,c,d = 10,20,30,40


# Day-2: Exercise-02

# 1. Check the data type of all your variables using type() built-in function
print(type(firstName))
print(type(lastName))
print(type(fullName))
print(type(age))
print(type(city))
print(type(country))
print(type(is_married))
print(type(is_light_on))
print(type(is_true))
print(type(year))

# 2. Using the len() built-in function, find the length of your first name
print(len(firstName))

# 3. Compare the length of your firstname and lastname

firstNameLength = len(firstName)
lastNameLength = len(lastName)

is_equal = firstNameLength==lastNameLength

"""4. Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division"""

num_one = 5
num_two = 4

total = num_one + num_two
print(total)

diff = num_one - num_two
print(diff)

product = num_one*num_two
print(product)

division = num_one/num_two
print(division)

exp = num_one **num_two
print(exp)

floor_division = num_one // num_two
print(floor_division)

remainder = num_one % num_two
print(remainder)

""" 5. The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area. """

radius = 30

area_of_circle = 3.14 * (radius **2) 

circum_of_circle = 2 * 3.14 * (radius**2)

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = input("Enter you first name: ")
last_name = input("enter your last name: ")
country = input("enter your country name:")
age = input("enter your age: ")

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

help('keywords')