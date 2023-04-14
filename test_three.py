# create a class called Hesabu to accept all the properties that are necessary
# to calculate both simple interest of a loan borrowed
# and volume of any cylinder
# implement the respective funcions to calculate the volume of a cylinder
# and the SI of a loan borrowed.
# NOTE: All data should come from the user as the input


class Hesabu:
    principle = input("Enter the principle\n")
    rate = input("Enter the rate\n")
    time = input("Enter the period in years\n")

    converted_principle = float(principle)
    converted_rate = float(rate)
    converted_time = float(time)

    simple_interest = (converted_principle * converted_rate * converted_time)/100
    print("The simple interest is", simple_interest)

    pi = 3.142
    radius = input("Enter the radius\n")
    height = input("Enter the height\n")

    converted_radius = float(radius)
    converted_height = float(height)

    volume = pi * pow(converted_radius, 2) * converted_height
    print("The volume of the cylinder is", volume)
