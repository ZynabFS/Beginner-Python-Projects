Questions = [
    ("Sound travels faster in what?","Air"),
    ("What is the only even prime number?","1"),
    ("How many bones are in the human body?","206"),
    ("What is the biggest planet in our solar system?","Jupiter"),
    ("What is the rarest blood type in humans?","AB-Negative")
]

for question, right_answer in Questions:
    answer = input(f"{question} ")
    if answer == right_answer:
        print("Correct!")

    else:
        print(f"The correct answer was {right_answer!r} ,not {answer!r}")