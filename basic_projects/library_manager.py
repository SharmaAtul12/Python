# Library Manager
# Manage books, issue records, and basic library statistics

books = []


def shorten_text(text, width):
    if len(text) <= width:
        return text
    return text[: width - 3] + "..."


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()

    if not title or not author:
        print("Title and author are required!")
        return

    books.append({
        "title": title,
        "author": author,
        "available": True,
        "borrower": "",
    })
    print(f"\nAdded: {title} by {author}")


def view_books():
    if not books:
        print("\nNo books in the library yet!")
        return

    print(f"\n{'No.':<5} {'Title':<25} {'Author':<20} Status")
    print("-" * 75)
    for index, book in enumerate(books, 1):
        status = "Available" if book["available"] else f"Issued to {book['borrower']}"
        print(
            f"{index:<5} {shorten_text(book['title'], 25):<25} "
            f"{shorten_text(book['author'], 20):<20} {status}"
        )


def search_book():
    if not books:
        print("\nNo books in the library yet!")
        return

    keyword = input("Enter title or author keyword: ").strip().lower()
    if not keyword:
        print("Please enter a keyword!")
        return

    matches = []
    for index, book in enumerate(books, 1):
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            matches.append((index, book))

    if not matches:
        print("\nNo matching books found!")
        return

    print(f"\nFound {len(matches)} matching book(s):")
    print("-" * 75)
    for index, book in matches:
        status = "Available" if book["available"] else f"Issued to {book['borrower']}"
        print(
            f"{index:<5} {shorten_text(book['title'], 25):<25} "
            f"{shorten_text(book['author'], 20):<20} {status}"
        )


def issue_book():
    view_books()
    if not books:
        return

    try:
        index = int(input("\nEnter book number to issue: "))
        if not 1 <= index <= len(books):
            print("Invalid book number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    book = books[index - 1]
    if not book["available"]:
        print(f"Book is already issued to {book['borrower']}!")
        return

    borrower = input("Enter borrower name: ").strip()
    if not borrower:
        print("Borrower name cannot be empty!")
        return

    book["available"] = False
    book["borrower"] = borrower
    print(f"Issued '{book['title']}' to {borrower}.")


def return_book():
    view_books()
    if not books:
        return

    try:
        index = int(input("\nEnter book number to return: "))
        if not 1 <= index <= len(books):
            print("Invalid book number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    book = books[index - 1]
    if book["available"]:
        print("This book is already available in the library!")
        return

    borrower = book["borrower"]
    book["available"] = True
    book["borrower"] = ""
    print(f"Returned '{book['title']}' from {borrower}.")


def remove_book():
    view_books()
    if not books:
        return

    try:
        index = int(input("\nEnter book number to remove: "))
        if not 1 <= index <= len(books):
            print("Invalid book number!")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    book = books[index - 1]
    if not book["available"]:
        print("Return the book before removing it from the library!")
        return

    removed = books.pop(index - 1)
    print(f"Removed: {removed['title']}")


def library_summary():
    if not books:
        print("\nNo books in the library yet!")
        return

    total = len(books)
    available = sum(book["available"] for book in books)
    issued = total - available
    authors = len({book["author"].strip().lower() for book in books})

    print("\nLibrary Summary")
    print("-" * 30)
    print(f"Total books:        {total}")
    print(f"Available books:    {available}")
    print(f"Issued books:       {issued}")
    print(f"Unique authors:     {authors}")


def main():
    print("=" * 40)
    print("        LIBRARY MANAGER")
    print("=" * 40)

    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Remove Book")
        print("7. Library Summary")
        print("8. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            remove_book()
        elif choice == "7":
            library_summary()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()