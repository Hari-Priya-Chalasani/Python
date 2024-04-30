# Day- 4 : Exercise-01

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty","Days","Of","Python")

# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding for All")

#  3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)

# 5. Print the length of the company string using len() method and print()
length = len(company)
print(length)

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print("Capitalized: ",company.capitalize())
print("Swapcase: ",company.swapcase())

# 9. Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find("Coding"))

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","coding"))

# 12. Replace the word coding in the string 'Coding For All' to Python.
message = "Python for Everyone"
print(message)
print(message.replace("Python for everyone","Python for All"))

# 13. Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
Company_List = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(Company_List.split())

# 15. What is the character at index 0 in the string Coding For All.
print(company[0])

# 16. What is the last index of the string Coding For All.
print("Last Index: ",length - 1)

# 17. What character is at index 10 in "Coding For All" string.
print(company[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.

words = message.split()
acronym = ' '.join([word[0].upper() for word in words])
print("Acronym/Abbrevation:",message,"is:",acronym)

# 19. Create an acronym or an abbreviation for the name 'Code for All'.
words = company.split()
acronym = ' '.join([word[0].upper() for word in words])
print("Acronym/Abbrevation:",company,"is:",acronym)

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
new_word = "You cannot end a sentence with because because because is a conjunction"
print(new_word.find("because"))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_word.rfind("because"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_word[31:54])

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(new_word.find("because"))

# 27. Does ''Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# 28. Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# 29. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
new_company = "   Coding For All      "
print(new_company.strip(" "))

# 30. Which one of the following variables return True when we use the method isidentifier():
        # 30DaysOfPython
        # thirty_days_of_python
sentence_one = "30DaysOfPython"
sentence_two = "thirty_days_of_python"
print(sentence_one.isidentifier())
print(sentence_two.isidentifier())

# 31. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
new_list = '# '.join(libraries_list)
print(new_list)

""" 32. Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next."""

print('I am enjoying this challenge.\nI just wonder what is next')

"""33. Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""

print('radius = 10\narea = 3.14 * radius ** 2\nThe area of a circle with radius 10 is 314 meters square.')

"""34. Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""

print('8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')

# 
