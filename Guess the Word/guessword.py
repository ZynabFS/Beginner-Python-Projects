
total_guesses = 3
current_guesses = 0
guess = ""
actual_word = "python"
out_of_guesses = False

while guess != actual_word and not(out_of_guesses):
    if current_guesses < total_guesses:
        guess = input("Enter a guess Word: ")
        current_guesses += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose! You are out of guesses.")

else:
    print("You Won!")
        