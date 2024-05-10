# defining the guessNum here.

guessNum = 0
answer = False

while not answer:
    guessNum = input("Enter a Guess Number: ") # writig the guessNum's input inside the loop to make the loop work.
    if int(guessNum) < 99:
        print("Too Low!") # their guess was wrong.

    elif int(guessNum) > 99:
        print("Too High!") # their guess was still wrong.

    else:
        print("Done")
        answer = True  # we got the correct answer, so exit the loop.
     # if the answer was false, that means the while loop will continue.
