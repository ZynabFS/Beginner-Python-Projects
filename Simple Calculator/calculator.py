#adding float here so the code will remain short and simple

num1 = float(input("Enter first digit: "))
num2 = float(input("Enter second digit: "))
operator = input("Enter an operator: ")

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

elif operator == "**":
    print(num1 ** num2)

elif operator == "%":
    print(num1 % num2)

else:
    print("Invalid Number or Operator!")