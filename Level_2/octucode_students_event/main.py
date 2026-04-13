
# Read the starting letter
with open("Input/Letters/starting_letter.txt", "r") as file:
    starting_letter = file.read()

# Read the names of the students
with open("Input/Names/invited_names.txt", "r") as file:
    names = file.readlines()

# For each name, create a personalized letter and save it
for name in names:

    name = name.strip()
    personalized_letter = starting_letter.replace("{name}", name).replace("{signature}", "Abdelrahman Ahmed")

    # Save the personalized letter
    with open(f"Output/Ready_to_send/letter_for_{name}.txt", "w") as file:
        file.write(personalized_letter)

    # Print the path of the generated letter    
    print(f"Generated letter for {name}: Output/Ready_to_send/letter_for_{name}.txt")
