# simple Calculator
def calculator():
    print("====Simple Calculator====")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose Operation: +,-,*,/")
    operation = input("Enter Operation: ")

    if operation == "+":
        result = num1 + num2

    elif operation == "-":
        result = num1 - num2

    elif operation == "*":
        result = num1 * num2

    elif operation == "/":
        if num2 == 0:
            print ("Eror! cant divide by zero")
            return
        result = num1 / num2

    else:
        print("Invalid Operation")
    
    print(f"Result: {result}")



if __name__ == "__main__":
    calculator()

