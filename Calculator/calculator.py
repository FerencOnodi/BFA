'''def get_input():
    user_input = int(input("Type in number: "))
    return user_input                              # Az egész függvény egy számmal egyenlő! amit a user ad meg!


def add_five(number):
    print(int(number) + 5)


add_five(get_input()) # Így kell értéket átadni egyik függvényből a másikba!
'''


def get_input1():
    num1 = float(input("Give me the first number: "))
    return num1


def get_input2():
    num2 = float(input("Give me the second number: "))
    return num2


def add(number1, number2):
    result = number1 + number2
    print(result)


def substract(number1, number2):
    result = number1 - number2
    print(result)


def multiply(number1, number2):
    result = number1 * number2
    print(result)


def divide(number1, number2):
    result = number1 / number2
    print(result)


def print_menu():
    print("\nMain menu: \n1. Add \n2. Substract \n3. Multiply \n4. Divie \n5. Exit")


def menu():
    print_menu()
    choose_option = input("\nChoose an option: ")

    if choose_option == "1":
        add(get_input1(), get_input2())
    elif choose_option == "2":
        substract(get_input1(), get_input2())
    elif choose_option == "3":
        multiply(get_input1(), get_input2())
    elif choose_option == "4":
        divide(get_input1(), get_input2())
    elif choose_option == "5":
        exit()


def main():
    while True:
        menu()
main()
