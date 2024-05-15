# Day- 5 : Exercise-01

# 1. Declare an empty list
first_list = []

# 2. Declare a list with more than 5 items
second_list = ["apple","banana","mango","orange","pine apple","strawberry","grapes"]

# 3. find the length of the list
print("Length of the list is: ",len(second_list))

# 4. Get the first item , last item and middle item of the list
first_item = second_list[0]
middle_item = second_list[3]
last_item = second_list[6]

print(first_item)
print(middle_item)
print(last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["priya",21,5.2,"Single","India"]

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]

# 7. Print the list using print()
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle and last company
first_item = it_companies[0]
middle_item = it_companies[3]
last_item = it_companies[6]

print(first_item)
print(middle_item)
print(last_item)

# 10. Print the list after modifying one of the companies
it_companies[3] = "Texas"
print(it_companies)

# 11. add an it company to it_companies list
it_companies.append("Apple")
print(it_companies)

# 12. Insert an IT company in the middle of the companies list