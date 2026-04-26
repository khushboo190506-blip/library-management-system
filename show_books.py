from data import books

def show_books():
    print("\n===== BOOK LIST =====")

    for book_id, book in books.items():
        status = "Available" if book["available"] else "Issued"
        print(f"{book_id}. {book['title']} -> {status}")