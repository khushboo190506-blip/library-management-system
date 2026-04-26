from data import books, issued
from utils import parse_date
from fine import calculate_fine

def return_book():
    print("\n--- RETURN BOOK ---")

    book_id = int(input("Enter Book ID: "))

    if book_id not in issued:
        print("This book was not issued!")
        return

    return_date_str = input("Enter Return Date (DD-MM-YYYY): ")
    return_date = parse_date(return_date_str)

    record = issued[book_id]
    due_date = record["due_date"]

    fine = calculate_fine(due_date, return_date)

    books[book_id]["available"] = True
    del issued[book_id]

    print("\nBook Returned Successfully!")
    print("Student:", record["student"])
    print("Due Date:", due_date.strftime("%d-%m-%Y"))
    print("Return Date:", return_date_str)

    if fine > 0:
        print("Fine: ₹", fine)
    else:
        print("No Fine (returned on time)")