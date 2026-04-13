# ===== Build the library ===== #
library = []
book_name = input("Enter the name of a book you own: ")
library.append(book_name)

other_book_name = input("Enter the name of another book you own (or press 'Enter' to skip): ")
if other_book_name:
    library.append(other_book_name)

print(f"\nLibrary: {library} \n")

# ===== Build the wishlist ===== #
wish_list = []
wish_book = input("Enter the name of a book you wish to have in the future (or press 'Enter' to skip): ")

if wish_book:
    wish_list.append(wish_book)

other_wish_book = input("Enter the name of another book you wish to have in the future (or press 'Enter' to skip): ")
if other_wish_book:
    wish_list.append(other_wish_book)

print(f"\nWishlist: {wish_list} \n")

#===== Update library and wishlist ===== #
acquired_book = input("Enter a name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if acquired_book in wish_list:
    library.append(acquired_book)
    wish_list.remove(acquired_book)

print(f"\nUpdated Library: {library}")
print(f"Updated Wishlist: {wish_list} \n")

# ===== Donate a book ===== #
donate_book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if donate_book in library:
    library.remove(donate_book)
    print(f"\n'{donate_book}' has been donated from your library.")

print(f"\nFinal library after donation: {library}")