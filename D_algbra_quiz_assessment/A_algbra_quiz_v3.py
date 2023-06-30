import time
import random

# cheacks floats
from _Functions.E_float_checker import float_check

from _Functions.A_int_checker import int_check

# generates a statement with a text / tittle and a symbol
from _Functions.C_statement_generator import statement_generator

# check if input is in valid list
from _Functions.D_choice_checker import choice_checker, yes_no_list


# displays instructions
def instructions():
    statement_generator("Here's how this Quiz works", "-", 3)
    print('''
- Firstly you will choose a difficulty
      (Easy, Normal or hard)
- Then you will be asked a series of 12 questions
  (The numbers in the questions and the questions order will be random)
- To answer these questions you need to find out what numbers X Y and Z are
  (The questions will allways have one variable(X), somtimes have two variables(X and Y),
   and might even have three variables(X,Y and Z) depending on the difficulty you chose)
- Next you will be given your results and a ✔️ to ❌ comparison and %
- Lastly you will be asked if you want to play again
  (If yes the entire program will repeat)

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

    difficulty_list = ["easy", "normal", "hard"]

    difficulty = choice_checker("chose a difficulty (Easy, Normal or Hard): ", difficulty_list, "please enter easy, "
                                                                                                "normal or hard")

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
    time.sleep(1)
    question_num = 1
    results = []
    questions_right = 0
    questions_wrong = 0
    ran_num = 0
    ran_num_2 = 0
    ran_num_3 = 0

    wanted_questions = int_check("how many question do you want: ", low=0, exit_code="xxx")
    wanted_questions += 1
    while True:
        print()

        statement_generator(f"Question {question_num}", "-+", lines=3)
        question_num += 1

        print("")
        if difficulty == "easy":

            # creates random numbers
            answer_Y = ""
            answer_X = ""
            ran_num = random.randint(0, 10)
            ran_num_2 = random.randint(0, 10)

            # list of available questions
            question_list = [
                f"{ran_num} + X = {ran_num_2}",
                f"X + X = {ran_num}",
                f"{ran_num} + {ran_num_2} = X"
            ]

            # chooses a random question from <question_list>
            question = random.choice(question_list)

            # corrects equations
            if question == f"{ran_num} + X = {ran_num_2}":
                ran_num_2 = random.randint(int(ran_num), 10)
                X = ran_num - ran_num_2
                question = f"{ran_num} + X = {ran_num_2}"
                questiono = f"{ran_num} + X = {ran_num_2}"

            elif question == f"X + X = {ran_num}":
                X = ran_num / 2
                questiono = question

            elif question == f"{ran_num} + {ran_num_2} = X":
                X = ran_num + ran_num_2
                questiono = question

            else:
                questiono = question

            # prints question
            print(f"{question}")
            print("")

            # asks for answer, makes answer a string and exits if answer is <xxx>
            while answer_X == "" or answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                answer_X = float_check("What is X: ", exit_code="xxx")
                if answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                    print("cant divide by zero")

            answer_X = str(answer_X)
            if answer_X == "xxx":
                break

            answer_Y = str(answer_Y)

            if answer_Y == "xxx":
                break

            # redys answer to be checked
            question = question.replace("X", answer_X)
            question = question.split(' = ')

            # checks answer
            if eval(question[0]) == eval(question[-1]):
                print("")
                print("correct")

            else:
                print("")
                print("wrong")

        elif difficulty == "normal":

            # creates random numbers
            answer_Y = ""
            answer_X = ""
            ran_num = random.randint(0, 50)
            ran_num_2 = random.randint(0, 50)

            # list of available questions
            question_list = [
                f"{ran_num} + X = {ran_num_2}",
                f"X + X = {ran_num}",
                f"{ran_num} + {ran_num_2} = X",
                f"{ran_num} * X = {ran_num_2}",
                f"{ran_num}/X = {ran_num_2}"
            ]

            # chooses a random question from <question_list>
            question = random.choice(question_list)

            # corrects equations
            if question == f"{ran_num} + X = {ran_num_2}":
                ran_num_2 = random.randint(int(ran_num), 50)
                X = ran_num - ran_num_2
                question = f"{ran_num} + X = {ran_num_2}"
                questiono = f"{ran_num} + X = {ran_num_2}"

            elif question == f"X + X = {ran_num}":
                X = ran_num / 2
                questiono = question

            elif question == f"{ran_num} + {ran_num_2} = X":
                X = ran_num + ran_num_2
                questiono = question

            elif question == f"{ran_num} * X = {ran_num_2}":
                ran_num = random.randint(0, 10)
                X = random.randint(0, 5)
                ran_num_2 = ran_num * X
                question = f"{ran_num} * X = {ran_num_2}"
                questiono = f"{ran_num}X = {ran_num_2}"

            elif question == f"{ran_num}/X = {ran_num_2}":
                ran_num_2 = random.randint(0, 10)
                X = random.randint(0, 5)
                ran_num = ran_num_2 * X
                question = f"{ran_num}/X = {ran_num_2}"
                questiono = f"{ran_num} ÷ X = {ran_num_2}"

            else:
                questiono = question

            # prints question
            if question == f"{ran_num} * X = {ran_num_2}" or \
                    question == f"{ran_num}/X = {ran_num_2}":
                print(f"{questiono}")
                print("")

            else:
                print(f"{question}")
                print("")

            # asks for answer, makes answer a string and exits if answer is <xxx>
            while answer_X == "" or answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                answer_X = float_check("What is X: ", exit_code="xxx")
                if answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                    print("cant divide by zero")

            answer_X = str(answer_X)
            if answer_X == "xxx":
                break

            answer_Y = str(answer_Y)

            if answer_Y == "xxx":
                break

            # redys answer to be checked
            question = question.replace("X", answer_X)
            question = question.split(' = ')

            # checks answer
            if eval(question[0]) == eval(question[-1]):
                print("")
                print("correct")

            else:
                print("")
                print("wrong")

        elif difficulty == "hard":

            # creates random numbers
            answer_Y = ""
            answer_X = ""
            ran_num = random.randint(-120, 120)
            ran_num_2 = random.randint(-120, 120)
            ran_num_3 = random.randint(-120, 120)

            # list of available questions
            question_list = [
                f"{ran_num} + X = {ran_num_2}",
                f"X + X = {ran_num}",
                f"{ran_num} + {ran_num_2} = X",
                f"{ran_num} * X = {ran_num_2}",
                f"{ran_num}/X = {ran_num_2}",
                f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}",
                f"{ran_num}/X/Y = {ran_num_2}"
            ]

            # chooses a random question from <question_list>
            question = random.choice(question_list)

            # corrects equations
            if question == f"{ran_num} + X = {ran_num_2}":
                ran_num_2 = random.randint(int(ran_num), 120)
                X = ran_num - ran_num_2
                question = f"{ran_num} + X = {ran_num_2}"
                questiono = f"{ran_num} + X = {ran_num_2}"

            elif question == f"X + X = {ran_num}":
                X = ran_num / 2
                questiono = question

            elif question == f"{ran_num} + {ran_num_2} = X":
                X = ran_num + ran_num_2
                questiono = question

            elif question == f"{ran_num} * X = {ran_num_2}":
                ran_num = random.randint(-20, 20)
                X = random.randint(-6, 6)
                ran_num_2 = ran_num * X
                question = f"{ran_num} * X = {ran_num_2}"
                questiono = f"{ran_num}X = {ran_num_2}"

            elif question == f"{ran_num}/X = {ran_num_2}":
                ran_num_2 = random.randint(-20, 20)
                X = random.randint(-6, 6)
                ran_num = ran_num_2 * X
                question = f"{ran_num}/X = {ran_num_2}"
                questiono = f"{ran_num} ÷ X = {ran_num_2}"

            elif question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}":
                ran_num = random.randint(-6, 6)
                ran_num_2 = random.randint(-6, 6)
                X = random.randint(-10, 10)
                Y = random.randint(-10, 10)
                ran_num_3 = ran_num * X + ran_num_2 * Y
                question = f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}"
                questiono = f"{ran_num}X + {ran_num_2}Y = {ran_num_3}"

            elif question == f"{ran_num}/X/Y = {ran_num_2}":
                ran_num_2 = random.randint(-10, 10)
                X = random.randint(-3, 3)
                Y = random.randint(-4, 4)
                ran_num = ran_num_2 * X
                ran_num = ran_num * Y
                if X == 0 or Y == 0:
                    ran_num_2 = 0
                question = f"{ran_num}/X/Y = {ran_num_2}"
                questiono = f"{ran_num} ÷ X ÷ Y = {ran_num_2}"

            else:
                questiono = question

            # prints question
            if question == f"{ran_num} * X = {ran_num_2}" or \
                    question == f"{ran_num}/X = {ran_num_2}" or \
                    question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}" or \
                    question == f"{ran_num}/X/Y = {ran_num_2}":
                print(f"{questiono}")
                print("")

            else:
                print(f"{question}")
                print("")

            # asks for answer, makes answer a string and exits if answer is <xxx>
            while answer_X == "" or answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                answer_X = float_check("What is X: ", exit_code="xxx")
                if answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                    print("cant divide by zero")

            if question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}" \
                    or question == f"{ran_num}/X/Y = {ran_num_2}":
                answer_Y = float_check("What is Y: ", exit_code="xxx")

            answer_X = str(answer_X)
            if answer_X == "xxx":
                break

            answer_Y = str(answer_Y)

            if answer_Y == "xxx":
                break

            # redys answer to be checked
            if question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}" \
                    or question == f"{ran_num}/X/Y = {ran_num_2}":
                question = question.replace("Y", answer_Y)
            question = question.replace("X", answer_X)
            question = question.split(' = ')

            # checks answer
            if eval(question[0]) == eval(question[-1]):
                print("")
                print("correct")

            else:
                print("")
                print("wrong")

        # not enogh time to finish
        elif difficulty == "insane":

            # creates random numbers
            answer_Y = ""
            answer_X = ""
            ran_num = random.randint(-250, 250)
            ran_num_2 = random.randint(-250, 250)
            ran_num_3 = random.randint(-250, 250)
            ran_num_4 = random.randint(-250, 250)
            ran_num_power = random.randint(-5, 5)

            # list of available questions
            question_list = [
                # f"{ran_num} + X = {ran_num_2}",
                # f"X + X = {ran_num}",
                # f"{ran_num} + {ran_num_2} = X",
                # f"{ran_num} * X = {ran_num_2}",
                # f"{ran_num}/X = {ran_num_2}",
                # f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}",
                # f"{ran_num}/X/Y = {ran_num_2}",
                f"(X + {ran_num}) ** {ran_num_power} / (Y * {ran_num_2} + {ran_num_3}) = {ran_num_4}",
                # f"{ran_num} * X / {ran_num_2} * Y + Z ** {ran_num_power} = {ran_num_3}"
            ]

            # chooses a random question from <question_list>
            question = random.choice(question_list)

            # corrects equations
            if question == f"{ran_num} + X = {ran_num_2}":
                ran_num_2 = random.randint(int(ran_num), 120)
                question = f"{ran_num} + X = {ran_num_2}"

            elif question == f"{ran_num} * X = {ran_num_2}":
                ran_num = random.randint(-20, 20)
                ran_num_2 = ran_num * random.randint(-6, 6)
                question = f"{ran_num} * X = {ran_num_2}"
                questiono = f"{ran_num}X = {ran_num_2}"

            elif question == f"{ran_num}/X = {ran_num_2}":
                ran_num_2 = random.randint(-20, 20)
                ran_num = ran_num_2 * random.randint(-6, 6)
                question = f"{ran_num}/X = {ran_num_2}"
                questiono = f"{ran_num} ÷ X = {ran_num_2}"

            elif question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}":
                ran_num = random.randint(-6, 6)
                ran_num_2 = random.randint(-6, 6)
                ran_num_3 = random.randint(-120, 120)
                question = f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}"
                questiono = f"{ran_num}X + {ran_num_2}Y = {ran_num_3}"

            elif question == f"{ran_num}/X/Y = {ran_num_2}":
                ran_num_2 = random.randint(-10, 10)
                ran_num = ran_num_2 * random.randint(-3, 3)
                ran_num = ran_num * random.randint(-4, 4)
                question = f"{ran_num}/X/Y = {ran_num_2}"
                questiono = f"{ran_num} ÷ X ÷ Y = {ran_num_2}"

            elif question == f"(X + {ran_num}) ** {ran_num_power} / (Y * {ran_num_2} + {ran_num_3}) = {ran_num_4}":
                questiono = f"(X + {ran_num})^{ran_num_power} ÷ (Y x {ran_num_2} + {ran_num_3}) = {ran_num_4}"

            else:
                print()

            # prints question
            if question == f"{ran_num} * X = {ran_num_2}" or \
                    question == f"{ran_num}/X = {ran_num_2}" or \
                    question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}" or \
                    question == f"{ran_num}/X/Y = {ran_num_2}" or \
                    question == f"(X + {ran_num}) ** {ran_num_power} / (Y * {ran_num_2} + {ran_num_3}) = {ran_num_4}":
                print(f"{questiono}")
                print("")

            else:
                print(f"{question}")
                print("")

            # asks for answer, makes answer a string and exits if answer is <xxx>
            while answer_X == "" or answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                answer_X = float_check("What is X: ", exit_code="xxx")
                if answer_X == 0 and question == f"{ran_num}/X/Y = {ran_num_2}":
                    print("cant divide by zero")

            if question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}" \
                    or question == f"{ran_num}/X/Y = {ran_num_2}" \
                    or question == f"(X + {ran_num}) ** {ran_num_power} / (Y * {ran_num_2} + {ran_num_3}) = {ran_num_4}":
                answer_Y = float_check("What is Y: ", exit_code="xxx")

            answer_X = str(answer_X)
            if answer_X == "xxx":
                break

            answer_Y = str(answer_Y)

            if answer_Y == "xxx":
                break

            # redys answer to be checked
            if question == f"{ran_num} * X + {ran_num_2} * Y = {ran_num_3}" \
                    or question == f"{ran_num}/X/Y = {ran_num_2}" \
                    or question == f"(X + {ran_num}) ** {ran_num_power} / (Y * {ran_num_2} + {ran_num_3}) = {ran_num_4}":
                question = question.replace("Y", answer_Y)
            question = question.replace("X", answer_X)
            question = question.split(' = ')

            # checks answer
            if eval(question[0]) == eval(question[-1]):
                print("")
                print("correct")

            else:
                print("")
                print("wrong")

            if question_num == 13:
                break

        else:
            print()

        if eval(question[0]) != eval(question[-1]):
            if questiono == f"{ran_num}X + {ran_num_2}Y = {ran_num_3}" or \
                    questiono == f"{ran_num} ÷ X ÷ Y = {ran_num_2}":
                results.append(f'''  Question {question_num - 1}: {questiono}
- Your answer for X was {answer_X}
- Your answer for Y was {answer_Y}
- A correct answer for X and Y is:
    X = {X} and Y = {Y}
''')
            elif questiono == f"{ran_num}X = {ran_num_2}" or \
                    questiono == f"{ran_num} ÷ X = {ran_num_2}":
                results.append(f'''  Question {question_num - 1}: {questiono}
- Your answer for X was {answer_X}
- The correct answer for X was {X}
''')
            elif questiono == f"{ran_num} + X = {ran_num_2}" or \
                    questiono == f"X + X = {ran_num}" or \
                    questiono == f"{ran_num} + {ran_num_2} = X":
                results.append(f'''  Question {question_num - 1}: {questiono}
- Your answer for X was {answer_X}
- The correct answer for X was {X}
''')
            questions_wrong += 1

        elif eval(question[0]) == eval(question[-1]):
            if questiono == f"{ran_num}X + {ran_num_2}Y = {ran_num_3}" or \
                    questiono == f"{ran_num} ÷ X ÷ Y = {ran_num_2}":
                results.append(f'''  Question {question_num - 1}: {questiono}
- Your answer for X was {answer_X}
- Your answer for Y was {answer_Y}
- Your answers were correct
''')
            elif questiono == f"{ran_num}X = {ran_num_2}" or \
                    questiono == f"{ran_num} ÷ X = {ran_num_2}":
                results.append(f'''  Question {question_num - 1}: {questiono}
- Your answer for X was {answer_X}
- your answer is correct
''')
            elif questiono == f"{ran_num} + X = {ran_num_2}" or \
                    questiono == f"X + X = {ran_num}" or \
                    questiono == f"{ran_num} + {ran_num_2} = X":
                results.append(f'''  Question {question_num - 1}: {questiono}
- Your answer for X was {answer_X}
- Your answer is correct
''')

            questions_right += 1

        if question_num == wanted_questions:
            break

    correct_percent = questions_right / (wanted_questions - 1)
    correct_percent *= 100
    correct_percent = int(correct_percent)

    print("")
    print(f'''You got {questions_right}/{(wanted_questions - 1)}correct '''
          f'''which is {correct_percent} out 100 percent''')

    show_history = choice_checker("Would you like to see you results: ", yes_no_list, "please enter yes or no as your "
                                                                                      "response")

    if show_history == "yes":
        print("")
        print("")
        print("|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|")
        print("|:*:|:*:|:*:|:*:|:*:| Quiz  results |:*:|:*:|:*:|:*:|:*:|")
        print("|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|:*:|")
        print("")

        for i in range(0, len(results)):
            print(results[i])

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
