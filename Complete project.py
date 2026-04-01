# Library Book Indexing System using Hash Table

library = {}   # Hash table

def add_book():
    isbn = input("Enter ISBN: ")
    if isbn in library:
        print("Book already exists!")
        return

    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = int(input("Enter Publication Year: "))
    copies = int(input("Enter Number of Copies: "))

    library[isbn] = {
        "title": title,
        "author": author,
        "year": year,
        "copies": copies
    }
    print("Book added successfully!")

def search_book():
    isbn = input("Enter ISBN to search: ")
    if isbn in library:
        book = library[isbn]
        print("\nBook Found:")
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Copies:", book["copies"])
    else:
        print("Book not found!")

def delete_book():
    isbn = input("Enter ISBN to delete: ")
    if isbn in library:
        del library[isbn]
        print("Book deleted successfully!")
    else:
        print("Book not found!")

def display_books():
    if not library:
        print("Library is empty!")
        return

    print("\nLibrary Books:")
    for isbn, book in library.items():
        print("\nISBN:", isbn)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Copies:", book["copies"])

def main():
    while True:
        print("\n--- Library Book Indexing System ---")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Delete Book")
        print("4. Display All Books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            display_books()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")

main()
