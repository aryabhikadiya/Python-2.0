# # Try except block
# try:
#     num1 = 10
#     num2 = 0 
#     result = num1 / num2
# except ZeroDivisionError:
#     print("The number can not be divided by zero")

# # multiple exceptions
# try:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter another number:"))
#     result = num1 / num2
#     print("The answer is {}".format(result))
# except ZeroDivisionError:
#     print("The number can not be divided by zero")
# except ValueError:
#     print("The number you have entered is invalid")

# # nessted tryexcept block
# try:
#     num1 = int(input("Enter a number:"))
#     num2 = int(input("Enter another number:"))
#     try:
#         result = num1/num2
#         print("The answer is {}".format(result))
#     except ZeroDivisionError:
#         print("The number can not be divided by 0")
# except ValueError:
#     print("The number you have entered is invalid")

# raise your exceptions
try:
    age = int(input("What is your age:"))
    if age<0:
        raise ValueError("Your age is not valid")
    else:
        print("Your age is valid")
except ValueError as e:
    print(e)




