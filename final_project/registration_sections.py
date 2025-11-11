"""
    Creating a program that will allow students to register for classes. Will read in
    a list of classes. 
    Will have a student class and a section class. Students will enter their information
    There will be an external file with a list of class sections read into the program
    Will
        1. get student info
        2. confirm
        3. load class sections
        4. display topic areas on screen 
        5. Ask user which area they want to select from (menu)
        6. Display list of classes - menu
        7. Select by typing course number or done when done
        8. Verify
        9. Generate and print billing statement (with fees, tuition, etc.)


"""

class Student:
    """ Student class here - address, phone, name, email"""
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, grade_level="Freshman"):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__grade_level = grade_level

    # Getter and Setter for first_name
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
        
    def get_student_id(self):
        return self.__student_id
    
    def get_grade_level(self):
        return self.__grade_level

    def set_first_name(self, value):
        self.__first_name = value
    
    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value
    
    def set_grade_level(self, value):
        self.__grade_level = value

    # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))
    
    # Method to print basic info about the student
    def print_info(self):
        print(self.__first_name + " " + self.__last_name)
        print(self.__student_id)
        print(self.__grade_level)

    def mailing(self):
        """All mailing labels"""

    def tuition_reminder(self):
        """Create bill"""

class Section:
    """ contains section information, class name, times, instructor etc."""
    def __init__(self, course_name, number, section, subject = "ADD"):
        # Instance variables
        self.__course_name = course_name
        self.__number = number
        self.__section = section
        self.__subject = subject

    # Getter and Setter for first_name
    def get_course_name(self):
        return self.__course_name
    
    def get_number(self):
        return self.__number
    
    def get_section(self):
        return self.__section
    
    def get_subject(self):
        return self.__subject
    
    def set_course_name(self, value):
        self.__course_name = value

    def set_number(self, value):
        self.__number = value

    def set_section(self, value):
        self.__section = value

    def set_subject(self, value):
        self.__subject = value
    
        # Method to print basic info about the section
    def print_info(self):
        print(f"{self.__subject}{self.__number}-{self.__section} {self.__course_name}")
        
    

def directions():
    """ print a welcome message with directions on screen"""

def student_info():
    """ Get student info, create an object with it"""
    # pass information into class student
    studentID = 1
    return studentID

def display_classes():
    """ load available course sections from file, create an object for each one """

def select_classes():
    """lets them pick classes from menu add to a list"""

def verify_info():
    """ Will display information on screen ask if they want to change student or course info"""

def billing():
    """Create bill"""
def main():
    """ Organizes logic flow """
    directions() # calls the directions functioin
    student_info() # get student information
    display_classes()
    select_classes()
    verify_info()
    billing()

    class1 = Section("Programming Logic", "100", "001", "ADD")
    class1.print_info()


main()