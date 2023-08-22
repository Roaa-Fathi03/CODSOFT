import time
import random

score = 0
asked_questions = []


def generate_random_number():
    return random.randint(0, 49)


def check_performance(round_no, p_score):
    if round_no == 2:
        if p_score >= int(.85 * 20):
            print("You are EXCELLENT!")
        elif p_score >= int(.7 * 20):
            print("You are REMARKABLE!")
        else:
            print("You are GOOD, try better next time!")

    elif round_no == 3:
        if p_score >= int(.85 * 30):
            print("WOW, You are GOLD!")
        elif p_score >= int(.7 * 30):
            print("Well Done, You are SILVER!")
        else:
            print("You are IRON, try better next time!")
    elif round_no == 4:
        if p_score >= int(.85 * 40):
            print("WOW, You are GENIUS!")
        elif p_score >= int(.7 * 40):
            print("Well Done, You are SMART!")
        else:
            print("You are NEWBIE, try better next time!")


def check_answer(correct_answer, answer):
    global score
    if answer == correct_answer:
        print("*** CORRECT ANSWER ***")
        score = score + 1
        time.sleep(1)
    else:
        print("** WRONG ANSWER **")
        print(f"The correct answer is {correct_answer.capitalize()}")
        time.sleep(1)

    print("\n")


def display_mcq_qs(my_file):
    lines = my_file.readlines()
    question_no = 1
    while question_no < 11:
        random_q = generate_random_number()
        # print(random_q)
        while random_q in asked_questions:
            random_q = generate_random_number()
        asked_questions.append(random_q)

        data = lines[random_q].split("/")
        questions = data[1]
        answer_a = data[2]
        answer_b = data[3]
        answer_c = data[4]
        answer_d = data[5]
        correct_answer = str(data[6]).strip().lower()
        print("*************** Score ******************")
        print(f"                 {score}")
        print(f"============ Question # {question_no} =============")
        print(questions)
        time.sleep(0.5)
        print("a)", answer_a)
        time.sleep(0.5)
        print("b)", answer_b)
        time.sleep(0.5)
        print("c)", answer_c)
        time.sleep(0.5)
        print("d)", answer_d)
        time.sleep(0.5)

        answer = str(input("Answer? ")).strip().lower()
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        check_answer(correct_answer, answer)
        question_no = question_no + 1
    my_file.close()


def display_fib__qs(my_file):
    lines = my_file.readlines()

    question_no = 1
    while question_no < 11:
        random_q = generate_random_number()
        # print(random_q)
        while random_q in asked_questions:
            random_q = generate_random_number()
        asked_questions.append(random_q)

        data = lines[random_q].split("/")
        questions = data[1]
        correct_answer = str(data[2]).strip().lower()

        print("*************** Score ******************")
        print(f"                 {score}")
        print(f"============ Question # {question_no} =============")
        print(f"{questions} ..........")
        answer = str(input("Answer? ")).strip().lower()

        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")

        check_answer(correct_answer, answer)

        question_no = question_no + 1

    my_file.close()


def display_rules():
    print("======================== WELCOME TO QUIZ! ========================")
    print("======================== Game Rules  ============================= \n"
          "1. Choose either multiple-choice or fill-in-the-blank questions.\n"
          "2. Choose a specific topic.\n"
          "3. Choose only one answer.\n"
          "4. Enter the specified data type.\n"
          "5. Maximum Number of rounds is 4 and minimum is 2.\n"
          "6. Each round is 10 questions in specific topic.\n"
          "==================================================================\n")


def display_fields():
    q_type = None
    while q_type is None:
        try:
            print("Choose...\n"
                  "1) Multiple-Choice Questions.\n"
                  "2) fill-in-the-blank Questions.\n")

            q_type = int(input("Enter either 1 or 2: "))
            if q_type not in [1, 2]:
                q_type = None
                print("Please enter 1 or 2!")
        except ValueError:
            print("Enter an integer number!")

        print("\n")

    choice = None
    while choice is None:
        try:
            print("============= Choose a Topic =============== \n"
                  "1) General Questions.\n"
                  "2) Medicine Questions.\n"
                  "3) History Questions.\n"
                  "4) Sports Questions.\n")

            choice = int(input("Enter a valid number: "))

            if choice not in range(1, 5):
                choice = None
                print("Enter number in the range 1 to 4!")

        except ValueError:
            print("Enter an integer number!")
        print("\n")

    mcq_files = ["GeneralQuestions-mcq.txt", "Medicine-mcq.txt", "History-mcq.txt", "Sports-mcq.txt"]
    fib_files = ["GeneralQuestions-fib.txt", "Medicine-fib.txt", "History-fib.txt", "Sports-fib.txt"]

    if q_type == 1:
        if choice in range(1, 5):
            file = open(mcq_files[choice - 1], "r")
            display_mcq_qs(file)
        else:
            print("Please enter a valid number!")

    elif q_type == 2:
        if choice in range(1, 5):
            file = open(fib_files[choice - 1], "r")
            display_fib__qs(file)
        else:
            print("Please enter a valid number!")

    else:
        print("Enter a valid choice!!")


def quiz_game():
    display_rules()

    display_rules()

    round_no = None
    while round_no is None:
        try:
            round_no = int(input("Enter the Number of Rounds (review rules):"))
            if round_no < 2 or round_no > 4:
                round_no = None
                print("Review the rules then enter a valid round number.\n")
        except ValueError:
            print("Enter an integer number.\n")

    rounds = round_no
    while round_no > 0:
        display_fields()
        round_no -= 1

    print("==============================\n"
          "          YOUR SCORE          \n"
          "==============================\n")
    print(f"             {score}\n"
          f"=============================\n")

    check_performance(rounds, score)


quiz_game()

