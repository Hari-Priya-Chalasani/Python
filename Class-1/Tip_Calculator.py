def main():
    amount = input("How much was the meal? $")
    percentage = input("What percentage would you like to tip?  ")
    tip = float(amount) * float(percentage)
    print(f"Leave:{tip:.2f}")
def amount():
    amount = float(amount)
    return amount
def percentage():
    percentage = float(percentage)
    percentage = ((percentage/amount)* 100)
    return percentage
main()
