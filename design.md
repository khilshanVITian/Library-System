# Design and Documentation

## Functional Modules
1.Displaying books
2.Adding books
3.Searching available books
4.Removing books
5.Exiting program

## System Architecture

User
  |
  v
main.py
  |
  v
runs program
## Workflow Diagram

Start
  |
  v
Display Menu
  |
  v
Select Operation
  |
  +--> Display books
  |
  +--> Add books
  |
  +--> Search books
  |
  +--> Remove books
  |
  +-->Exit
  v
Validate Input
  |
  v
Update Data
  |
  v
Return to Menu

## Use Case Diagram

             +-----------------------------+
             |   Library Management System |
             +-----------------------------+
              /       |        |        \
             /        |        |         \
        Display      Add   Search     Remove
         books      books   books    books
           ^          ^        ^          ^
           |          |        |          |
        Librarian / Library Administrator

### Books
`id, name, author, available`
