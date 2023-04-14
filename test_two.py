# create a function to ascertain that the user has "eMobilis" as username and "eMobilis@123" as the password
# Henceforth, proceed to calculate the BMI of the user and display the results of the
# BMI as either 1. Underweight, 2. Normal Weight 3. Overweight or 4. Obese
# NOTE All the data should be provided by the user as input.
# Use the scale below for the BMI
#           0 -------18------- Underweight
#           18.1-----29-------- Normal weight
#           29.1------ 34 ------- Overweight
#           34.1-------- and above ---- Obese





username = input("Enter the username\n")
password = input("Enter the password\n")

if username == "eMobilis" and password == "eMobilis@123":
    print("Logged in successfully")
    weight = input("Enter your weight\n")
    height = input("Enter your height\n")
    converted_weight = float(weight)
    converted_height = float(height)
    BMI = converted_weight / pow(converted_height, 2)
    if BMI <= 18:
        print("Underweight")
    elif BMI <= 29:
        print("Normal weight")
    elif BMI <= 34:
        print("Overweight")
    else:
        print("Obese")
else:
    print("You have entered an invalid username or password")