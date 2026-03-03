def search_book():
    isbn = input("Enter ISBN to search: ")

    if isbn in library:
        book = library[isbn]
        print("\nBook Found")
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Copies:", book["copies"])
    else:
        print("Book not found!")
