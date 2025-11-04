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
    

class Section:
    """ contains section information, class name, times, instructor etc."""
    
    

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