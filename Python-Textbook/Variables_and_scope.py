a = 0


def my_function():
    global a  # mivel a globális változó, a következő sor felülírja a 0 értéket 3-ra!
    a = 3
    print(a)

my_function()

print(a)
# ^ Bad practice, don't use global variables!!

# Exercise 1.
# 1.    a: global variable, passed in as an argument False// Local variable
#       b: local variable
#       c: gloabal variable
#       d: local variable False // global variable mivel csak if-en belül van
#
# 2.    a: exists while my_function is executed
#       b: exists while my_funciton is executed
#       c: exists while the program is running
#       d: created after checking the if statement, exists till the program is running
#
# 3.    The program would not print anything.
#
# 4.    Pass, bullshit :)

try:
    height = int(input("Enter height of rectangle: "))
    width = int(input("Enter width of rectangle: "))
    print("The area of the rectangle is: %d" % (width * height))
except ValueError as e:  # if a value error occurs, we will skip to this point
    print("Error reading height and width: %s" % e)
    # This will only ask the user for input once, if it fails, won't try again.a


correct_input = False  # this is a boolean value -- it can be either true or false.

while not correct_input:  # this is a while loop
    try:
        height = int(input("Enter height of rectangle: "))
        width = int(input("Enter width of rectangle: "))
        print("The area of the rectangle is: %d" % (width * height))
    except ValueError:
        print("Please enter valid integers for the height and width.")
    else:  # this will be executed if there is no value error
        correct_input = True
        # This will ask again until the input is valid.


# Exercise 2.

valid_input = False

while not valid_input:
    try:
        f_degree = float(input("Enter the degree in fahrenheit: "))
        print("%d Fahrenheit equals %d Celsius degree." % (f_degree, (5 / 9 * (f_degree - 32))))
    except ValueError:
        print("Please enter a valid integer or float.")
    else:
        valid_input = True


# Exercise 3.

a = float("8.8")
a = round(8.8)
a = round(int("8.8"))
a = str(8.8)
a = str(8)
a = bool(8)
