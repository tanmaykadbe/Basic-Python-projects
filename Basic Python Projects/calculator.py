num1 = int(input("Please enter a number: "))
operator = input("Please enter an operator: /*+-: ")
num2 = int(input("Please enter a number: "))
 
if operator == "+":
    print(f"The sum is {num1 + num2}")
elif operator == "-":
    print(f"The difference is{num1 - num2}")
elif operator == "*":
    print(f"The product is {num1*num2}")
elif operator == "/":
    print(f"The quotient is {num1/num2}")
else:
    print("Please recheck the operator or the numbers")