operators = input("Enter an operator (+, -, *, /): ")
number1 = float(input("Enter the number 1 : "))
number2 = float(input("Enter the number 2 : "))

if operators == "+":
    result = number1 + number2
    print(round(result, 3))
elif operators == "-":
    result = number1 - number2
    print(round(result, 3))
elif operators == "*":
    result = number1 * number2
    print(round(result, 3))
elif operators=="/":
    result = number1 / number2
    print(round(result, 3))
else:
    print(f"{operators} is an invalid number")
    
    
