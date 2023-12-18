# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.


greeting = input("Greeting: ")
greet = greeting.lower()
start_with_hello = greet.find("hello")
start_with_h = greet.find('h')

if start_with_hello == 0:
    print("$0")
elif start_with_h == 0 or start_with_h == -1:
    print("$20")
else:
    print("$100")