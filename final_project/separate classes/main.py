"""
main.py
-------
Main program for the Final Project.

This file imports Student and Section and organizes the entire program flow.

IMPORTANT:
    • Students will complete the placeholder functions in class.
    • All user input belongs in this file.
    • No class definitions appear here.

Program Flow:
    1. directions()
    2. student_info()
    3. display_classes()
    4. select_classes()
    5. verify_info()
    6. billing()
"""

from Student import Student
from Section import Section

# ----------------------------------------------------------------------
# Placeholder Functions (completed in class together)
# ----------------------------------------------------------------------

def directions():
    """Print welcome message and basic instructions.

    STUDENT MODIFICATION POINT:
        Students will create a meaningful welcome screen or menu here.
    """
    pass


def student_info():
    """Collects user data, creates a Student object, and saves it.

    STUDENT MODIFICATION POINT:
        Students may add data validation (checking numbers, trimming spaces, etc.)
    """
    print("We need to get some basic information to register you for class.")

    fname = input("First name: ")
    lname = input("Last name: ")
    sid = int(input("Student ID: "))
    phone = input("Phone (###-###-####): ")
    email = input("Email: ")
    street = input("Street Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip Code: ")

    stu = Student(fname, lname, sid, phone, email,
                  street, city, state, zip_code)

    stu.save_to_file()
    print("\nStudent information recorded.\n")


def display_classes():
    """Loads available classes from a file and creates Section objects.

    STUDENT MODIFICATION POINT:
        In class, students will:
            • open the sections file
            • read each line
            • split the line
            • create Section objects
            • store them in a list
    """
    pass


def select_classes():
    """Allows student to pick classes from a menu.

    STUDENT MODIFICATION POINT:
        • Loop through available sections
        • Let user type course numbers
        • Store selections
    """
    pass


def verify_info():
    """Displays all gathered info for confirmation.

    STUDENT MODIFICATION POINT:
        • Display all selected sections
        • Ask if student wants to edit info
    """
    pass


def billing():
    """Calculates tuition and prints a bill.

    STUDENT MODIFICATION POINT:
        • Decide on tuition rates
        • Multiply by number of credits
        • Format bill output
    """
    pass


# ----------------------------------------------------------------------
# Main Program
# ----------------------------------------------------------------------

def main():
    """Controls the flow of the program."""
    directions()
    student_info()
    display_classes()
    select_classes()
    verify_info()
    billing()

  


# Run the program
main()
