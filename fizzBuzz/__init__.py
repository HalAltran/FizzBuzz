from fizzBuzz.FizzList import FizzList
from fizzBuzz.FizzObject import FizzObject


def multiple_of(dividend, divisor):
    return dividend % divisor == 0


def list_contains_string(parent_list, string_to_match):
    return any(entry == string_to_match for entry in parent_list)


def fizz_buzz(user_input_line):

    input_entries = user_input_line.split(",")

    for x in range(1, 301):
        fizz_list = FizzList()

        if list_contains_string(input_entries, str(3)) and multiple_of(x, 3):
            fizz_list.add_object(FizzObject("Fizz", False, False, 1))

        if list_contains_string(input_entries, str(5)) and multiple_of(x, 5):
            fizz_list.add_object(FizzObject("Buzz", False, False, 3))

        if list_contains_string(input_entries, str(7)) and multiple_of(x, 7):
            fizz_list.add_object(FizzObject("Bang", False, False, 4))
        if list_contains_string(input_entries, str(11)) and multiple_of(x, 11):
            fizz_list.add_object(FizzObject("Bong", True, True, 5))

        if list_contains_string(input_entries, str(13)) and multiple_of(x, 13):
            fizz_list.add_object(FizzObject("Fezz", True, False, 2))

        if list_contains_string(input_entries, str(17)) and multiple_of(x, 17):
            fizz_list.reverse = True
            
        print("x = " + str(x) + ": " + fizz_list.format_output())


user_input = input("Enter only integers separated by commas: ")
print(user_input)
fizz_buzz(user_input)
