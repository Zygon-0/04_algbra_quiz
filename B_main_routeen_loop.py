import time

# check if input is in valid list
from _Functions.D_choice_checker import choice_checker, yes_no_list


# Main routine goes here
while True:

    #

    play_again = choice_checker("would you like to run the program again: ", yes_no_list, "please enter yes or no as "
                                                                                          "your response")
    if play_again == "yes":
        print("")
    elif play_again == "no":
        break

print("")
print("thanks for playing")
time.sleep(1)
