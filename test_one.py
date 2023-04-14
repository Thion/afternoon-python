# Write a logic to implement a simple calculator
# capable of computing two numbers entered by the user as input
# Make sure the program can compute with either of the four mathematical operations


first_number = input("Enter the first number\n")
first_number = int(first_number)

operation = input("Input the intended operation\n")

second_number = input("Enter the second number\n")
second_number = int(second_number)
if operation == "+":
    print("The answer is", first_number + second_number)
elif operation == "-":
    print("The answer is", first_number - second_number)
elif operation == "*":
    print("The answer is", first_number * second_number)
elif operation == "/":
    print("The answer is", first_number / second_number)
else:
    print("Enter any of these operations +-*/")

