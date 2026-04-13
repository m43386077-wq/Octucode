import os

users = []
WELCOME_MESSAGE = """
Welcome to the User Management System!

Choose an action:

1. Add new user
2. View all users
3. Exit

"Enter your choice (1-3): """

class User:

    def __init__(self, first_name, last_name, email, status='inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.status = status

    def display_user_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Status: {self.status}")
        print()
        print("=" * 20)
        print()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_user():
    clear_screen()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    users.append(User(first_name, last_name, email))
    print("\nUser added successfully!\n")
    input("Press Enter to continue...")

def display_all_users():
    clear_screen()
    if not users:
        print("No users found.")
    else:
        print("Displaying all users...\n")
        for user in users:
            user.display_user_info()
    input("Press Enter to continue...")

while True:

    clear_screen()
    choice = input(WELCOME_MESSAGE)

    if choice == '1':
        add_user()

    elif choice == '2':
        display_all_users()

    elif choice == '3':
        print("\nExiting the User Management System. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 3.")
        input("Press Enter to continue...")
