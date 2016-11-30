from get_input import my_input


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print_fizzbuzz()
    elif number % 3 == 0:
        print_fizz()
    elif number % 5 == 0:
        print_buzz()
    else:
        print("Your number is not divisable with 3 nor 5. Try again with an other number!")


def print_fizz():
    print("Fizz")


def print_buzz():
    print("Buzz")


def print_fizzbuzz():
    print("FizzBuzz")


def main():
    while True:
        fizzbuzz(my_input())
main()
