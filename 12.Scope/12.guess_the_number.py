"""1.  Ask for difficulty
	Easy  - 10 attempts
	or
	Hard - 5 attempts

2. Computer random number  bw  1 and 100


While
3.  user_inpu = Ask the user to guess the number

4 print the ruels
	Make a guess: {user_input}
	Too hight/ Too low
	Guess again.

	You have {attempts} remaining to guess the number
	Make a guess: {user_input}


5. You've run out of guesses, you lose
or
You win """

'''1.  Ask for difficulty'''

import random

def ask_for_level_of_difficulty():
    difficulty = input("Type 'hard' or 'easy': ")
    user_attempts = 0
    if difficulty == "hard":
        user_attempts = 5
    else:
        user_attempts = 10
    return user_attempts


def generate_number():
    return random.randint(1, 100)

def ask_user_to_guess(target_number, user_attempts):
    user_number = int(input("Please guess the computer number: "))
    print(f"Make a guess: {user_number}")
    user_guess_the_number = False

    if user_number > target_number:
        print("Too hight")
    elif user_number < target_number:
        print("Too low")
    elif user_number == target_number:
        user_guess_the_number = True

    print(f"You have {user_attempts - 1} remaining to guess the number")
    return user_guess_the_number

def play_the_game(user_attempts, target_number):
    user_win = False
    game_is_over = False
    while not game_is_over:
        game_is_over = ask_user_to_guess(target_number, user_attempts)

        if game_is_over:
            user_win = True
            break
        user_attempts -= 1
        if user_attempts == 0:
            game_is_over = True

    return user_win

def  print_output(user_win):
    if user_win == False:
        print("You've run out of guesses, you lose")
    else:
        print("You win")

def start_game():
    user_attempts = ask_for_level_of_difficulty()
    target_number = int(generate_number())
    user_win = play_the_game(user_attempts, target_number)
    print_output(user_win)

start_game()

