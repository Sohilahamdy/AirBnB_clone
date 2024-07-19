# AirBnB Clone - The Console

# Description
Welcome to the AirBnB clone project! This project aims to replicate the core
functionality of AirBnB using Python. The first step involves creating a
command-line interface(CLI) that manages various objects within ou
AirBnB application.

# Command Interpreter
The command interpreter allows users to perform the following operations:
    - Create new objects(e.g., User, Place)
- Retrieve objects from a file or database
- Perform operations on objects(e.g., count, compute stats)
- Update attributes of an object
- Destroy objects

# Getting Started
To start the command interpreter, follow these steps:
    1. Clone the repository:

        git clone https: // github.com/your_username/AirBnB_clone.git

Navigate into the project directory:
    cd AirBnB_clone

Launch the command interpreter:
    ./console.py

Usage
The command interpreter supports both interactive and non-interactive modes:

    Interactive Mode
    $./console.py
(hbnb) help

Documented commands(type help < topic >)

EOF help quit

(hbnb)
(hbnb) quit
$

Non-interactive Mode
$ echo "help" | ./console.py
(hbnb)

Documented commands(type help < topic >)

EOF help quit
(hbnb)

Examples
Here are a few examples of commands you can use in the AirBnB console:

    Creating a new object
    (hbnb) create User
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)

Showing an object
(hbnb) show User 6cfb47c4-a434-4da7-ac03-2122624c3762
[User](6cfb47c4-a434-4da7-ac03-2122624c3762)
{'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at':
    '2024-07-19T12:00:00', 'updated_at': '2024-07-19T12:00:00'}
(hbnb)

Updating an object
(hbnb) update User 6cfb47c4-a434-4da7-ac03-2122624c3762 email
"example@email.com"
(hbnb)

Deleting an object
(hbnb) destroy User 6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)

Authors
Sohila Hamdy - Developer & Project Lead

GitHub: https: // github.com/Sohilahamdy
Email: sohila.fathy22@gmail.com
Requirements
Python 3.8.5
Ubuntu 20.04 LTS
All Python scripts should be executable
Code should adhere to PEP8 style guidelines(use pycodestyle)
Use of unittest module for testing
Documentation for modules, classes, and functions
Copyright - Plagiarism
This project is designed to help you understand and implement various Python
concepts. Please refrain from plagiarism, as it violates the principles of
learning and will result in removal from the program.
