def display_books():
    if not library:
        print("Library is empty!")
        return

    print("\nLibrary Book List")
    for isbn, book in library.items():
        print("\nISBN:", isbn)
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Year:", book["year"])
        print("Copies:", book["copies"])
