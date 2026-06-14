# Exercise : Python Calculator

is_running = True

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{operator} is not a valid operator")

while is_running:
    done = input("Do you wana cantinue the calculations? (Y/N): ").upper()
    if not done == "Y":
        print(f"The total is: {result}")
        is_running = False
    else:
        operator = input("Enter an operator (+ - * /): ")
        num2 = float(input("Enter the 2nd number: "))
        if operator == "+":
            result += num2
            print(round(result, 3))
        elif operator == "-":
            result -= num2
            print(round(result, 3))
        elif operator == "*":
            result *= num2
            print(round(result, 3))
        elif operator == "/":
            result /= num2
            print(round(result, 3))
        else:
            print(f"{operator} is not a valid operator")
