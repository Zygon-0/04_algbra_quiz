import time
import random

# functions

# checks integers
from _Functions.A_int_checker import int_check

# displays instructions
from _Functions.B_instrucktions import instructions

# generates a statement with a text / tittle and a symbol
from _Functions.C_statement_generator import statement_generator

# check if input is in valid list
from _Functions.D_choice_checker import choice_checker, yes_no_list

# Main routine goes here
while True:
    play_again = choice_checker("would you like to run the program again: ", yes_no_list, "please enter yes or no as "
                                                                                          "your response")
    if play_again == "yes":
        print("")
    elif play_again == "no":
        break

print("")
print("thanks for playing")
time.sleep(1)
