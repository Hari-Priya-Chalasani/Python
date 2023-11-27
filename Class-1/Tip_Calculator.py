#defining main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#defining the function that is used to convert dollar value to float
def dollars_to_float(d):
    return float(d)

#defining the function that is used to convert percentage to float 
def percent_to_float(p):
    return float(p) / 100

#Calling main function 
main()

