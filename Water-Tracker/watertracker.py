wanna_exit = False
current_water = 0 
water_left = 2000

print("Welcome to Water Tracker")
print("You have drink '0ml'")

while True:

    command = input("Enter a command, i.e; 'see-water', 'water-left', 'add' or 'exit': ")

    if command == "see-water":
        print(f"{current_water}ml")

    elif command == "water-left":
        print(f"{water_left}ml")

    elif command == "add":
        adding_water = int(input("How much water did you drink? "))
        current_water = current_water + adding_water
        print(f"You have drank {adding_water}ml water.")
        water_left = water_left - adding_water

    elif command == "see-water":
        print(current_water)


    elif command == "exit":
        print("GoodBye!")
        break

    else:
        print("Invalid Input")