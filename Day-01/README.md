<h1>Introduction</h1>
Python is a high-level programming language for general-purpose programming. It is an open source, interpreted, objected-oriented programming language. Python was created by a Dutch programmer, Guido van Rossum. The name of Python programming language was derived from a British sketch comedy series, Monty Python's Flying Circus. The first version was released on February 20, 1991. This 30 days of Python challenge will help you learn the latest version of Python, Python 3 step by step. The topics are broken down into 30 days, where each day contains several topics with easy-to-understand explanations, real-world examples, many hands on exercises and projects.

<h1>Why Python ? </h1
It is a programming language which is very close to human language and because of that it is easy to learn and use. Python is used by various industries and companies (including Google). It has been used to develop web applications, desktop applications, system adminstration, and machine learning libraries. Python is highly embraced language in the data science and machine learning community. I hope this is enough to convince you to start learning Python. Python is eating the world and you are killing it before it eats you.
<h1>Basic Python</h1>
<h1>Python Syntax</h1>
A Python script can be written in Python interactive shell or in the code editor. A Python file has an extension .py.

<h1>Python Indentation </h1>
An indentation is a white space in a text. Indentation in many languages is used to increase code readability, however Python uses indentation to create block of codes. In other programming languages curly brackets are used to create blocks of codes instead of indentation. One of the common bugs when writing python code is wrong indentation.
<h1>Comments</h1>
Comments are very important to make the code more readable and to leave remarks in our code. Python does not run comment parts of our code. Any text starting with hash(#) in Python is a comment.

Example: Single Line Comment

    # This is the first comment
    # This is the second comment
    # Python is eating the world

Example: Multiline Comment

Triple quote can be used for multiline comment if it is not assigned to a variable

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""
<h1>Data types</h1>
In Python there are several types of data types. Let us get started with the most common ones. Different data types will be covered in detail in other sections. For the time being, let us just go through the different data types and get familiar with them. You do not have to have a clear understanding now.

<h1>Number</h1>
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j
<h1>String</h1>
A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

Example:

'Asabeneh'
'Finland'
'Python'
'I love teaching'
'I hope you are enjoying the first day of 30DaysOfPython Challenge'
<h1>Booleans</h1>
A boolean data type is either a True or False value. T and F should be always uppercase.

Example:

    True  #  Is the light on? If it is on, then the value is True
    False # Is the light on? If it is off, then the value is False

<h1>List</h1>
Python list is an ordered collection which allows to store different data type items. A list is similar to an array in JavaScript.

Example:

[0, 1, 2, 3, 4, 5] # all are the same data types - a list of numbers
['Banana', 'Orange', 'Mango', 'Avocado'] # all the same data types - a list of strings (fruits)
['Finland','Estonia', 'Sweden','Norway'] # all the same data types - a list of strings (countries)
['Banana', 10, False, 9.81] # different data types in the list - string, integer, boolean and float
<h1>Dictionary</h1>
A Python dictionary object is an unordered collection of data in a key value pair format.

Example:

{
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland',
'age':250,
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
<h1>Tuple</h1>
A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable.

Example:

('Asabeneh', 'Pawel', 'Brook', 'Abraham', 'Lidiya') # Names
('Earth', 'Jupiter', 'Neptune', 'Mars', 'Venus', 'Saturn', 'Uranus', 'Mercury') # planets

<h1>Set</h1>
A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Like in Mathematics, set in Python stores only unique items.

Example:

{2, 4, 3, 5}
{3.14, 9.81, 2.7} # order is not important in set
Checking Data types
To check the data type of certain data/variable we use the type function. In the following terminal you will see different python data types:

<h1>Checking Data types</h1>

Example:

The file name is helloworld.py

# Day 1 - 30DaysOfPython Challenge

print(2 + 3) # addition(+)
print(3 - 1) # subtraction(-)
print(2 _ 3) # multiplication(_)
print(3 / 2) # division(/)
print(3 ** 2) # exponential(**)
print(3 % 2) # modulus(%)
print(3 // 2) # Floor division operator(//)

# Checking data types

print(type(10)) # Int
print(type(3.14)) # Float
print(type(1 + 3j)) # Complex number
print(type('Asabeneh')) # String
print(type([1, 2, 3])) # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7})) # Set
print(type((9.8, 3.14, 2.7))) # Tuple
