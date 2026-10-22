print("Welcome to the SAFE CALCULATOR!")
while True:
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
    except ValueError:
        print("Please enter a valid number")
        continue
    try:
        operations = input("Choose an operation: + - * /: ")
        if operations == "+":
            results = num1 + num2

        elif operations == "-":
            results = num1 - num2


        elif operations == "*":
            results = num1 * num2

        
        elif operations == "/":
            results = num1 / num2

        else:
            raise ValueError("Enter a valid operations")
    except ZeroDivisionError:
        print("You can not divide a number by 0")
        continue
    except ValueError as e:
        print(e) 
        continue
    print(results)
