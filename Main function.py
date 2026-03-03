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
