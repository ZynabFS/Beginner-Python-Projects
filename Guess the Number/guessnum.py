guessNum = input("Enter a Guess Number: ")

#here we have add int with the guess number because we can't compare str and int together
if int(guessNum) < 10:
    print("Your Guessed Number is Lower than the Actual Number!")
    
elif int(guessNum) > 10:
    print("Your Guessed Number is Higher than the Actual Number!")

else:
    print("You Have Guessed The Actual Number")
