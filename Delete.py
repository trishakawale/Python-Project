def delete_book():
    isbn = input("Enter ISBN to delete: ")

    if isbn in library:
        del library[isbn]
        print("Book deleted successfully!")
    else:
        print("Book not found!")
