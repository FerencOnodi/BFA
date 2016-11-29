def main_menu():
    sub_menus = ["1. Add", "2. Subtract", "3. Multiply", "4. Divide", "5. Exit program\n"]
    for i in sub_menus:
        print(i)
    user_input = input("Choose an option!: ")

    if user_input == "1":
        add(num1, num2)
    elif user_input == "2":
        subtract(num1, num2)
    elif user_input == "3":
        multiply(num1, num2)
    elif user_input == "4":
        divide(num1, num2)
    elif user_input == "5":
        exit()
    else:
        error_message()

def error_message():
    print("\nPlease enter a valid option!\n")


def get_numbers():
    num1 = input("Please enter the first number! ")
    num2 = input("Please enter the second number! ")
    if type(num1) == str or type(num2) == str:
        error_message()       
    return num1, num2

def add(num1, num2): # csak így nem lehet átadni értékeket
    result = float(num1) + float(num2)
    return result

def subtract(num1, num2):
    result = float(num1) - float(num2)
    return result

def multiply(num1, num2):
    result = float(num1) * float(num2)
    return result

def divide(num1, num2):
    result = float(num1) / float(num2)
    return result

def main():
    while True:
        get_numbers()
        main_menu()
main()
