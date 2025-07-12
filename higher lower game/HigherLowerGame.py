import higherAndLowerGameData as data
import random



def format_data(account):
    """
    Format the account data into prinatble format.
    :param account: Account data
    :return: printable formatted data
    """
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, {account_description}, {account_country}")

def check_answer(user_guess, a_followers, b_followers):
    """
    Check whether the user guesses are correct or not.
    :param user_guess: the user guesses
    :param a_followers: the number of followers of first account
    :param b_followers: the number of followers of second account
    :return: whether the user guesses are correct or not
    """
    if a_followers > b_followers:
        return user_guess == "a"
    elif a_followers < b_followers:
        return user_guess == "b"


score = 0
game_flag = True
account_b = random.choice(data.game_data)


while(game_flag):
    account_a = account_b
    account_b = random.choice(data.game_data)
    if account_a == account_b:
        account_b = random.choice(data.game_data)

    print(f"Compare A: {format_data(account_a)}\n")
    print("Vs\n")
    print(f"Compare B: {format_data(account_b)}\n")

    user_guess = input("which account has more followers? 'A' or 'B'").lower()

    print("\n"*20) #clear the screen

    a_followers = account_a["followers"]
    b_followers = account_b["followers"]

    is_correct = check_answer(user_guess, a_followers, b_followers)

    if is_correct:
        score += 1
        print(f"you guessed correctly, your score is {score}")
    else:
        print(f"Sorry, you didn't guess correctly, your final score is {score}")
        game_flag = False
