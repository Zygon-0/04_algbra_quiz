# check if input is in valid list
import time


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

    play_again = choice_checker("would you like to run the program again", yes_no_list, "please enter yes or no as "
                                                                                        "your responce")
    if play_again == "yes":
        print("")
    elif play_again == "no":
        print("")
        print("thanks for playing")
        time.sleep(1)