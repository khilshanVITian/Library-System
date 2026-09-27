# Design and Documentation

## Functional Modules
1. Book Management
2. Member Management
3. Issue/Return Management
4. Search and Reporting
5. Data Storage and Validation

## System Architecture

```text
User
  |
  v
main.py
  |
  +--> book_manager.py
  +--> member_manager.py
  +--> transaction_manager.py
  +--> reports.py
  |
  +--> validators.py
  |
  v
storage.py
  |
  v
library_data.json
```

## Workflow Diagram

```text
Start
  |
  v
Display Menu
  |
  v
Select Operation
  |
  +--> Book Management
  |
  +--> Member Management
  |
  +--> Issue/Return
  |
  +--> Reports
  |
  v
Validate Input
  |
  v
Update Data
  |
  v
Save JSON Data
  |
  v
Return to Menu
```

## Use Case Diagram

```text
             +-----------------------------+
             |   Library Management System |
             +-----------------------------+
              /       |        |        \
             /        |        |         \
        Manage      Manage   Issue/     View
         Books     Members   Return    Reports
           ^          ^        ^          ^
           |          |        |          |
        Librarian / Library Administrator
```

## Component Diagram

```text
+-------------+       +----------------+
|   main.py   |------>| book_manager   |
+-------------+       +----------------+
       |              +----------------+
       +------------->| member_manager |
       |              +----------------+
       +------------->| transaction    |
       |              +----------------+
       +------------->| reports        |
       |              +----------------+
       |
       +------------->| validators     |
                      +----------------+
                              |
                              v
                      +----------------+
                      |    storage     |
                      +----------------+
                              |
                              v
                      library_data.json
```

## Sequence Example: Issue Book

```text
User -> main.py: Select Issue Book
main.py -> transaction_manager: issue_book()
transaction_manager -> validators: Validate IDs
transaction_manager -> storage: Save updated data
storage -> library_data.json: Write data
transaction_manager -> User: Confirmation
```

## Storage Schema

### Books
`id, name, author, available`

### Members
`id, name`

### Transactions
`book_id, member_id, issue_date, return_date, status`
