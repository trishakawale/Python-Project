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
