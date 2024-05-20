import random

print("Welcome to the Rock, paper and scissor game! ")

commands = ["rock", "paper", "scissor"]
out_of_rounds = False

while True:
    user_choice = input("Choose an option, 'rock', 'paper', 'scissor': ").lower()
    computer_choice = random.choice(commands)

    if user_choice == computer_choice:
        print(f"Its a tie!\nYou choosed '{user_choice}' and\n the computer choosed '{computer_choice}'")

    elif user_choice == "rock" and computer_choice == "scissor":
        print(f"You won!\nYou choosed '{user_choice}' and\n the computer choosed '{computer_choice}'")

    elif user_choice == "paper" and computer_choice == "rock":
        print(f"You won!\nYou choosed '{user_choice}' and\n the computer choosed '{computer_choice}'")

    elif user_choice == "scissor" and computer_choice == "paper":
        print(f"You won!\nYou choosed '{user_choice}' and\n the computer choosed '{computer_choice}'")

    else:
        print(f"You lose!\nYou choosed '{user_choice}' and\n the computer choosed '{computer_choice}'")

    play_again = input("Wanna play again? ").lower()
    if play_again == "no":
        print("GoodBye!")
        break