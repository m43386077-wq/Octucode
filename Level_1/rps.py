import random

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissor = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Welcome message and rules
print("Welcome to Rock, Paper, Scissors Game!")
help = input("Press 'Enter' to continue or type 'help' for the rules: ")
if help == "help":
    print("""
    ========== Rules ==========
    1) You choose and the comoputer randomly chooses one of the three options: Rock, Paper, or Scissors.
    2) Rock smashes Scissors -> Rock wins
    3) Scissors cuts Paper -> Scissors wins
    4) Paper covers Rock -> Paper wins
    ===========================
    """)

# computer choice
computer_choice = random.choice([rock, paper, scissor])

# user choice
user_choice = input("Choose Rock, Paper, or Scissors: ").lower()

if user_choice == "rock":
    user_choice = rock
elif user_choice == "paper":
    user_choice = paper
elif user_choice == "scissors":
    user_choice = scissor
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissors.")
    exit()

# Display choices
print(f"\nYou chose:\n{user_choice}")
print(f"Computer chose:\n{computer_choice}\n")

# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (
    (user_choice == rock and computer_choice == scissor) or
    (user_choice == paper and computer_choice == rock) or
    (user_choice == scissor and computer_choice == paper)
):
    print("You win!")
else:
    print("Computer wins!")
