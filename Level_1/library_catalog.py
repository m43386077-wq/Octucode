import os

catalog = []

def clear_screan():
    os.system("cls" if os.name == "nt" else "clear")

def add_book():
    clear_screan()
    book = {
        "isbn": input("Enter ISBN: "),
        "title": input("Enter title: "),
        "auther": input("Enter auther: "),
        "available": True,
    }
    catalog.append(book)
    print(f"\nBook '{book['title']}' by {book['auther']} added to the catalog with ISBN {book['isbn']}.\n")
    if input("Do you want to add another book? (y/n): ").lower() == "y":
        add_book()

def check_out_book():
    clear_screan()
    isbn = input("Enter ISBN to check out: ")
    for i in range(len(catalog)):
        book = catalog[i]
        if book["isbn"] == isbn:
            if not book["available"]:
                print(f"Book '{book["title"]}' is currently checked out.")
            else:
                catalog[i]["available"] = False
                print(f"Book '{book["title"]}' is checked out successfully.")
            break
    else:
        print("Book not fount in the catalog!")
    
    if input("Do you want to check out another book? (y/n): ").lower() == "y":
        check_out_book()

def check_in_book():
    clear_screan()
    isbn = input("Enter ISBN to check in: ")
    for i in range(len(catalog)):
        book = catalog[i]
        if book["isbn"] == isbn:
            if book["available"]:
                print(f"Book '{book["title"]}' is not checked out.")
            else:
                catalog[i]["available"] = True
                print(f"Book '{book["title"]}' is checked in successfully.")
            break
    else:
        print("Book not fount in the catalog!")

    if input("Do you want to check in another book? (y/n): ").lower() == "y":
        check_in_book()

def list_books():
    clear_screan()
    print("========== Books ==========")
    for book in catalog:
        print(f"ISBN: {book["isbn"]}")
        print(f"Title: {book["title"]}")
        print(f"Auther: {book["auther"]}")
        print(f"Available: {book["available"]}")
        print("=" * 27)
    input("Press 'Enter' if you want to back to the main menu...")

MENU = """
Menu:
1. Add book
2. Check Out Book
3. Check In Book
4. List Books
5. Exit
Enter your choice (1-5): """

while True:

    clear_screan()
    choice = input(MENU)

    if choice == "1":
        add_book()

    elif choice == "2":
        check_out_book()

    elif choice == "3":
        check_in_book()

    elif choice == "4":
        list_books()

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid Choice!")
