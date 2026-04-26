from data import books, issued
from utils import parse_date
from datetime import timedelta

def issue_book():
    print("\n--- ISSUE BOOK ---")

    book_id = int(input("Enter Book ID: "))

    if book_id not in books:
        print("Invalid Book ID")
        return

    if not books[book_id]["available"]:
        print("Book already issued")
        return

    student_name = input("Enter Student Name: ")
    issue_date_str = input("Enter Issue Date (DD-MM-YYYY): ")
    days = int(input("Issued for how many days: "))

    issue_date = parse_date(issue_date_str)
    due_date = issue_date + timedelta(days=days)

    issued[book_id] = {
        "student": student_name,
        "issue_date": issue_date,
        "due_date": due_date
    }

    books[book_id]["available"] = False

    print("\nBook Issued Successfully!")
    print("Student:", student_name)
    print("Due Date:", due_date.strftime("%d-%m-%Y"))

    print("\nNOTICE:")
    print("Week 1 → ₹10/day")
    print("Week 2 → ₹20/day")
    print("Week 3 → ₹60/day ...")