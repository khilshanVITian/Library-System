# Design and Documentation

## Functional Modules
1.Displaying books
2.Adding books
3.Searching available books
4.Removing books
5.Exiting program

## System Architecture

User-->main.py-->programme runs
## Workflow Diagram

Start-->displays menu-->select operation-->+display books
                                           +add books
                                           +search books
                                           +remove books
                                           +exit
                                           -->validate input-->update data-->return to menu
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
