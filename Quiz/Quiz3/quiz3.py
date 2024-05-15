Questions = {
    "Sound travels faster in what? ":[
        "Water", 
        "Air",
        "Vaccum",
        "None"
        ],

    "What is the only even prime number? ":[
        "2",
        "1",
        "3",
        "0"
        ],

    "How many bones are in the human body? ":[
        "206",
        "300",
        "205",
        "207"
        ],

    "What is the biggest planet in our solar system? ": [
        "Jupiter",
        "Mars",
        "Earth",
        "Pluto",
    ],
    "What is the rarest blood type in humans? ": [
        "AB-Negative",
        "O-Positive",
        "B-Negative",
        "O-Positive",
    ],
}

for question, alternative in Questions.items():
    right_answer = alternative[0]
    for alternative in sorted(alternative):
        print(f"{alternative}")

    answer = input(f"{question}")
    if answer == right_answer:
        print("Correct!")
    else:
        print(f"The correct answer was {right_answer!r} ,not {answer!r}")