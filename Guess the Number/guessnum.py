guessNum = input("Enter a Guess Number: ")

if int(guessNum) < 10:
    print("Your Guessed Number is Lower than the Actual Number!")
    
elif int(guessNum) > 10:
    print("Your Guessed Number is Higher than the Actual Number!")

else:
    print("You Have Guessed The Actual Number")




### Make a repo of it then make a same game but a guess number game with a hint on its 3rd time and game will be over after 5 trys