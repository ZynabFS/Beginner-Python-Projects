
permission = input("Do you wanna play a quiz game? ")
if permission == "Yes":
    print("Let's Go! ")

    q1 = input("Sound travels faster in what? ")
    if q1 == "Air":
        print("Correct!")
    else:
        print(f"The correct answer was 'Air', not {q1!r}")
        # these formatted strings literal are a way to format your string that is more readable and fast.

    q2 = int(input("What is the only even prime number? ")) # using 'int' so the input should be in number or if it won't be, this program will crash
    if q2 == 1:
        print("Correct!")
    else:
        print(f"The correct answer was '1', not {q2!r}")

    q3 = int(input("How many bones are in the human body? ")) # using the same thing (int) here. 
    if q3 == 206 :
        print("Correct!")
    else:
        print(f"The correct answer was '206', not {q3!r}")

    q4 = input("What is the biggest planet in our solar system? ")
    if q4 == "Jupiter":
        print("Correct!")
    else:
        print(f"The correct answer was 'Jupiter', not {q4!r}")

    q5 = input("What is the rarest blood type in humans? ")
    if q5 == "AB-Negative":
        print("Correct!")
    else:
        print(f"The correct answer was 'AB-Negative', not {q5!r}")
        print("That's a good game!")

elif permission == "No":
    print("Okay")

else:
    print("Invalid Input")