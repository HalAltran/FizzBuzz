from fizzBuzz.FizzList import FizzList


def multiple_of(dividend, divisor):
    return dividend % divisor == 0


def fizz_buzz():

    for x in range(1, 301):
        fizz_list = FizzList(x)

        if multiple_of(x, 3):
            fizz_list.add_object("Fizz")
        if multiple_of(x, 5):
            fizz_list.add_object("Buzz")
        if multiple_of(x, 7):
            fizz_list.add_object("Bang")
        if multiple_of(x, 11):
            fizz_list.add_object("Bong")
        if multiple_of(x, 13):
            fizz_list.add_object("Fezz")
        if multiple_of(x, 17):
            fizz_list.add_object("Reverse")

        print("x = " + str(x) + ": " + fizz_list.format_output())


fizz_buzz()
