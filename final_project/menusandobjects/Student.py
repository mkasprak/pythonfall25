"""
student.py
----------
Defines the Student class used in the Final Project.

This file mirrors the organization and documentation style of main.py.
Students should use it as a reference for how classes can contain
attributes (data), behavior (methods), and work with files.

IMPORTANT RULES FOR FINAL PROJECTS:
    • Classes NEVER contain input() statements.
    • Classes focus on storing data and performing actions on that data.
    • main.py handles all user interaction.
"""

# ----------------------------------------------------------------------
# 🧍 STUDENT CLASS — Represents one MCC student and all stored details
# ----------------------------------------------------------------------
class Student:
    """
    Represents a student registering for classes.

    Attributes (all private):
        first_name
        last_name
        student_id
        phone
        email
        street_address
        city
        state
        zip
    """

    # 🎓 Class-level attribute (shared by all students)
    school_name = "McHenry County College"

    # ------------------------------------------------------------------
    # 🏗️ INITIALIZER
    # Creates a new Student object and stores all attributes privately.
    # ------------------------------------------------------------------
    def __init__(self, first_name, last_name, student_id, phone, email,
                 street, city, state, zip_code):

        # 🔒 Private attributes (double underscore → name mangling)
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__phone = phone
        self.__email = email
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip = zip_code

    # ------------------------------------------------------------------
    # 📥 GETTERS (Accessor Methods)
    # Allow safe access to private attributes.
    # ------------------------------------------------------------------
    def get_first_name(self): return self.__first_name
    def get_last_name(self): return self.__last_name
    def get_student_id(self): return self.__student_id
    def get_phone(self): return self.__phone
    def get_email(self): return self.__email
    def get_street_address(self): return self.__street_address
    def get_city(self): return self.__city
    def get_state(self): return self.__state
    def get_zip(self): return self.__zip

    # ------------------------------------------------------------------
    # ✏️ SETTERS (Mutator Methods)
    # Used by verify/update steps in main.py to modify stored values.
    # ------------------------------------------------------------------
    def set_first_name(self, value): self.__first_name = value
    def set_last_name(self, value): self.__last_name = value
    def set_student_id(self, value): self.__student_id = value
    def set_phone(self, value): self.__phone = value
    def set_email(self, value): self.__email = value
    def set_street_address(self, value): self.__street_address = value
    def set_city(self, value): self.__city = value
    def set_state(self, value): self.__state = value
    def set_zip(self, value): self.__zip = value

    # ------------------------------------------------------------------
    # 🖨️ DISPLAY METHODS
    # Shown to the user during verification in main.py.
    # ------------------------------------------------------------------
    def print_info(self):
        """Prints a nicely formatted block of student information."""
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Email: {self.__email}   Phone: {self.__phone}")
        print(f"Address: {self.__street_address}, {self.__city}, "
              f"{self.__state} {self.__zip}")

    def print_info_numbered(self):
        """
        Numbered format for the update menu.
        Students pick a number to edit a field.
        """
        print(f"1. First Name:    {self.__first_name}")
        print(f"2. Last Name:   {self.__last_name}")
        print(f"3. Email:    {self.__email}")
        print(f"4. Phone:    {self.__phone}")
        print(f"5. Address:    {self.__street_address}")
        print(f"6. City:    {self.__city}")
        print(f"7. State:    {self.__state}")
        print(f"8. Zip:    {self.__zip}")

    # ------------------------------------------------------------------
    # 💾 FILE OUTPUT
    # Appends one student record to students.txt.
    # main.py controls WHEN writing happens.
    # ------------------------------------------------------------------
    def save_to_file(self):
        """
        Appends the student's information to students.txt.
        Stored as CSV-style data with commas.
        """
        with open("final_project/menusandobjects/students.txt", "a") as f:
            f.write(f"{self.__first_name},{self.__last_name},{self.__student_id},"
                    f"{self.__email},{self.__phone},{self.__street_address},"
                    f"{self.__city},{self.__state},{self.__zip}\n")
