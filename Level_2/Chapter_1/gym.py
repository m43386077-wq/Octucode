import os

members = []

WELCOME_MESSAGE = """
Welcome to the Gym Membership Management System!

Choose an action:

1. Add new member
2. View all members
3. Search for a member
4. Exit

"Enter your choice (1-3): """

SEARCH_BY = """
Search By:
                     
1. Membership ID
2. First Name
3. Status (active/inactive)
                       
Enter your choice (1-3): """

class Member:

    def __init__(self, first_name, last_name, id, status='inactive'):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.status = status

    def display_member_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Membership ID: {self.id}")
        print(f"Membership Status: {self.status}")
        print()
        print("=" * 20)
        print()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_member():
    clear_screen()
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    id = input("Enter membership ID: ")
    status = input("Enter membership status (active/inactive), or press 'Enter' for default: ").lower()
    members.append(Member(first_name, last_name, id, status if status in ['active', 'inactive'] else 'inactive'))
    print("\nMembership added successfully!\n")
    input("Press Enter to continue...")

def display_all_members():
    clear_screen()
    if not members:
        print("No members found.")
    else:
        print("Displaying all members...\n")
        for member in members:
            member.display_member_info()
    input("Press Enter to continue...")

def search_member():
    clear_screen()
    search_by = input(SEARCH_BY)

    if search_by == '1':
        id = input("Enter membership ID to search: ")
        found_members = [member for member in members if member.id == id]
    elif search_by == '2':
        first_name = input("Enter first name to search: ")
        found_members = [member for member in members if member.first_name.lower() == first_name.lower()]
    elif search_by == '3':
        status = input("Enter membership status to search (active/inactive): ").lower()
        found_members = [member for member in members if member.status == status]
    else:
        print("\nInvalid choice. Please enter a number between 1 and 3.")
        input("Press Enter to continue...")
        return
    
    if not found_members:
        print("\nNo members found matching the search criteria.")
    else:
        clear_screen()
        print("\nSearch results...\n")
        for member in found_members:
            member.display_member_info()
    input("\nPress Enter to continue...")

while True:

    clear_screen()
    choice = input(WELCOME_MESSAGE)

    if choice == '1':
        add_member()

    elif choice == '2':
        display_all_members()

    elif choice == '3':
        search_member()

    elif choice == '4':
        print("\nExiting the gym membership management system. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please enter a number between 1 and 4.")
        input("Press Enter to continue...")
