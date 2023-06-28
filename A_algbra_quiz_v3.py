import time

# generates a statement with a text / tittle and a symbol
from _Functions.C_statement_generator import statement_generator

# check if input is in valid list
from _Functions.D_choice_checker import choice_checker, yes_no_list


# displays instructions
def instructions():
    statement_generator("Here's how this Quiz works", "-", 3)
    print('''
- firstly you will chose a difficulty
- then you will be asked a series of 12 questions
  (the numbers in the questions and the questions order will be random)
- next you will be given your results
- and lastly you will be asked if you want to play again
  (if yes the entire program will repeat)

Good Luck   
    ''')


# Main routine goes here
while True:

    instructions_yes_no = choice_checker("Do you want to see the instructions: ", yes_no_list, "please enter yes or "
                                                                                               "no as your response")
    print("")

    if instructions_yes_no == "yes":
        instructions()
        print("")

    difficulty_list = ["easy", "normal", "hard", "insane", "wtf"]

    difficulty = choice_checker("chose a difficulty (Easy, Normal, Hard Insane or Wtf): ", difficulty_list,
                                "please enter easy, normal, "
                                "hard, insane or wtf as your "
                                "response")

    diff_emoji = ""

    if difficulty == "easy":
        diff_emoji = "😀Easy😀"

    elif difficulty == "normal":
        diff_emoji = "😐Normal😐"

    elif difficulty == "hard":
        diff_emoji = "😠Hard😠"

    elif difficulty == "insane":
        diff_emoji = "👿Insane👿"

    elif difficulty == "wtf":
        diff_emoji = "💀Wtf💀"

    print("")
    print(f"you chose {diff_emoji} difficulty")
    print("")

    play_again = choice_checker("would you like to run the program again: ", yes_no_list, "please enter yes "
                                                                                          "or no as your "
                                                                                          "response")

    if play_again == "yes":
        print("")
    else:
        break

print("")
print("thanks for playing")
time.sleep(1)
