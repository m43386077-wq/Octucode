print("""
_____________________________
     █    ███████    █
____██__ █████████ __██______
      █ ███████████ █
_______ ██_█████_██ _________
        ██  ███  ██
________███████████__________
      █  ████ ████  █
____██____██ █ ██____██______
     █    ██ █ ██    █
""")
print("Welcome to my island!")
print("There are two doors in front of you. 🚪 a red door and 🚪 a blue door.")
door_choice = input("Which door do you want to open? (red/blue): ").lower()

# Check the user's choice for the door
if door_choice == "red":
    print("Great! now you entered a room.")
    print("You found three boxes: ⬜ white box, ⬛ black box, and 🟩 green box.")
    box_choice = input("Which box do you open? (white/black/green): ").lower()

    # Check the user's choice for the box
    if box_choice == "white":
        print("Oops! You opened a box filled with snakes!")
        print("Game Over! 🐍🐍🐍")

    elif box_choice == "black":
        print("Oops! You opened a box filled with spiders!")
        print("Game Over! 🕷️🕷️🕷️")

    elif box_choice == "green":
        print("Congratulations! You found the treasure! 💎🏆🏆")
        
    else:
        print("Invalid choice! 🤷🤷🤷")

elif door_choice == "blue":
    print("Oops! You chose the crocodile door!")
    print("Game Over! 🐊🐊🐊")

else:
    print("Invalid choice! 🤷🤷🤷")
