from book_manager import add_book, display_books, search_book, remove_book, update_book
from member_manager import add_member, display_members, remove_member
from transaction_manager import issue_book, return_book, display_transactions
from reports import library_report
from storage import load_data


def main():
    data = load_data()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Remove Book")
        print("6. Add Member")
        print("7. Display Members")
        print("8. Remove Member")
        print("9. Issue Book")
        print("10. Return Book")
        print("11. View Transactions")
        print("12. Library Report")
        print("13. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_books(data)
        elif choice == "2":
            add_book(data)
        elif choice == "3":
            search_book(data)
        elif choice == "4":
            update_book(data)
        elif choice == "5":
            remove_book(data)
        elif choice == "6":
            add_member(data)
        elif choice == "7":
            display_members(data)
        elif choice == "8":
            remove_member(data)
        elif choice == "9":
            issue_book(data)
        elif choice == "10":
            return_book(data)
        elif choice == "11":
            display_transactions(data)
        elif choice == "12":
            library_report(data)
        elif choice == "13":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 13.")


if __name__ == "__main__":
    main()
