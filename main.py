books = [
    {"id":1,"name":"Programming for Engineers","author":"A.R. Bradley"},
    {"id":2,"name":"Introduction to the Design and Analysis of Algorithms","author":"Levitin"},
    {"id":3,"name":"Let Us Python","author":"Yashavant Kanetkar"},
    {"id":4,"name":"Higher Engineering Mathematics","author":"B. S. Grewal"},
    {"id":5,"name":"Advanced Engineering Mathematics","author":"Peter V. O’ Neil"},
    {"id":6,"name":"AI Revolution","author":"Andrew Tate"},
    {"id":7,"name":"Machine Learning","author":"Tom & Jerry"},
    {"id":8,"name":"Application Development","author":"Michael Jackson"},
    {"id":9,"name":"Cyber Security In Your Life","author":"Daniel Jr"},
    {"id":10,"name":"Wasting Time","author":"Khilshan W."}]

def display_books():
    print("\n--- Books available currently ---")
    if len(books) == 0:
        print("There are no books now.")
    else:
        for book in books:
            print("ID:", book["id"], "| Title:", book["name"], "| Author:", book["author"])
    print()
def add_book():
    print("\n--- Add a Book ---")
    book_id = int(input("Enter Book ID: "))

    for book in books:
        if book["id"] == book_id:
            print("Error: A book with this ID already exists!\n")
            return

    name = input("Please enter the book name: ")
    author = input("Please enter the author name: ")

    new_book = {
        "id": book_id,
        "name": name,
        "author": author}
    books.append(new_book)
    print("Book added successfully!\n")

def search_book():
    print("\n--- Search Book ---")
    search_name = input("Enter book name: ")
    found = False

    for book in books:
        if book["name"].lower() == search_name.lower():
            print("Match found:")
            print("ID:", book["id"])
            print("Name:", book["name"])
            print("Author:", book["author"])
            found = True
    if not found:
        print("No book found with that title.")
    print()

def remove_book():
    print("\n--- Remove Book ---")
    book_id = int(input("Enter Book ID to remove: "))
    found = False
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book removed successfully!\n")
            found = True
            break
    if not found:
        print("Book ID not found.\n")

while True:
    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Display Books")
    print("2. Add Book")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_books()
    elif choice == "2":
        add_book()
    elif choice == "3":
        search_book()
    elif choice == "4":
        remove_book()
    elif choice == "5":
        print("Thanks for your patience and precious time!")
        break
    else:
        print("Invalid choice! Please choose an option between 1 and 5.\n")
