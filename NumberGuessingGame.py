from random import randint

EASY_TURNS = 10
HARD_TURNS = 5

def check_win(user_guess, computer_guess):
    '''check if the user guesses correctly'''
    global win_flag
    if user_guess == computer_guess:
        print(f'You won!, The answer is {computer_guess}')
        win_flag = True
    elif user_guess > computer_guess:
        print("Too high!")
    elif user_guess < computer_guess:
        print("Too low!")

def set_difficulty():
    difficulty = input("Choose a difficulty easy or hard: ")
    if difficulty == 'easy':
        return EASY_TURNS
    elif difficulty == 'hard':
        return HARD_TURNS


#let the game randomly choose the number that the user has to guess
hidden_num = randint(1, 100)
win_flag = False


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turns = set_difficulty()
    global win_flag
    global play_again
    while turns > 0:
        #let the user enter his guess
        guessed_num = int(input("Make a guess: "))

        check_win(guessed_num, hidden_num)
        if win_flag:
            break
        turns -= 1
        print(f"You have {turns} guesses left")
    if(turns == 0) and (not win_flag):
        print("You are out of turns, you lost!")
    print("Do you want to play again?")
    play_again = input("Enter yes to play again or no to end the game: ")

play_again = "yes"
while(play_again == "yes"):
    game()

print("Thank you for playing!")