"""
student.py
----------
Defines the Student class used in the Final Project.

This file contains ONLY the Student class. It is separated so students can clearly 
see how classes are organized across multiple files.

Students Will Modify:
    • Add additional methods later (mailing labels, billing, validation, formatting).
    • Improve how data is written to the output file.
    • Optional: add more attributes if their final project requires them.

Important:
    • This file is imported by main.py.
    • Do NOT add input() statements inside a class — user interaction belongs in main.py.
"""

class Student:
    """
    Represents a student registering for classes.

    Attributes:
        first_name, last_name, student_id, phone, email
        street_address, city, state, zip
    """

    school_name = "McHenry County College"   # Class-level attribute

    def __init__(self, first_name, last_name, student_id, phone, 
                 email, street_address, city, state, zip):
        # Private attributes using name-mangling
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__email = email
        self.__phone = phone
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------
    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_id(self):
        return self.__student_id

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_street_address(self):
        return self.__street_address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    # ------------------------------------------------------------------
    # Setters
    # ------------------------------------------------------------------
    def set_first_name(self, value):
        self.__first_name = value

    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value

    def set_phone(self, value):
        self.__phone = value

    def set_email(self, value):
        self.__email = value

    def set_street_address(self, value):
        self.__street_address = value

    def set_city(self, value):
        self.__city = value

    def set_state(self, value):
        self.__state = value

    def set_zip(self, value):
        self.__zip = value

    # ------------------------------------------------------------------
    # Behavior Methods
    # ------------------------------------------------------------------
    def print_info(self):
        """Display a formatted line of student information."""
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Email: {self.__email}   Phone: {self.__phone}")
        print(f"Address: {self.__street_address}, {self.__city}, "
              f"{self.__state} {self.__zip}")
    
    def print_info_numbered(self):
        """Display a formatted line of student information."""
        print(f"1. {self.__first_name} \n2.  {self.__last_name} \n")
        print(f"3. Email: {self.__email} \n4.  Phone: {self.__phone} \n")
        print(f"5. Address: {self.__street_address} \n6. {self.__city} \n"
              f"7. {self.__state} \n8 {self.__zip}")

    def save_to_file(self):
        """
        Appends the student's information to a text file.

        Students Will Modify:
            • Add better formatting.
            • Use commas or tabs consistently.
            • Use write() multiple times or format strings neatly.
        """
        with open("final_project/menusandobjects/students.txt", "a") as f:
            f.write(f"{self.__first_name}, {self.__last_name}, {self.__student_id}, {self.__email}, "
                    f"{self.__phone}, {self.__street_address}, {self.__city}, "
                    f"{self.__state}, {self.__zip}\n")

