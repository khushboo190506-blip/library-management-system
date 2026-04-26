from data import books

def add_book():
    print("\n--- ADD BOOK ---")

    book_id = int(input("Enter Book ID: "))

    if book_id in books:
        print("Book already exists!")
        return

    title = input("Enter Book Title: ")

    books[book_id] = {
        "title": title,
        "available": True
    }

    print("Book added successfully!")