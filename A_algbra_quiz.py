import time
import random

# functions


# checks integers
def int_check(question, low=None, high=None, exit_code=None):

    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    if low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            # check that integer is valid (ie: not too low / too hig etc.)
            if situation == "any integer":
                return response

            elif situation == "both":
                if low <= response <= high:
                    return response

            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# displays instructions
def instructions():
    statement_generator("Here are the rules", "-", 3)
    print('''
- ...
- ...
- ...
- ...
- ...

Good Luck   
    ''')


# generates a statement with a text / tittle and a symbol
def statement_generator(statement, decoration, lines=None):
    middle = f'{decoration * 5} {statement} {decoration * 5}'

    if len(decoration) == 1:
        top_bottom = f'{decoration * len(middle)}'
    else:
        top_bottom = decoration * int(len(middle) / len(decoration) + 1)
        while len(middle) != len(top_bottom):
            top_bottom = top_bottom.rstrip(top_bottom[-1])

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    elif lines == 3:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# check if input is in valid list
def choice_checker(question, valid_list, error):
    while True:

        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output an error if item not in valid list
        print(error)
        print()


# choice checker lists
yes_no_list = ["yes", "no"]

# Main routine goes here
while True:
    play_again = choice_checker("would you like to run the program again: ", y, "please enter yes or no as "
                                                                                          "your response")
    if play_again == "yes":
        print("")
    elif play_again == "no":
        break

print("")
print("thanks for playing")
time.sleep(1)

