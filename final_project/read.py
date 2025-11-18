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
    """ Student class here """
    # Class variable
    school_name = "McHenry County College"

    def __init__(self, first_name, last_name, student_id, phone, email, street_address, city, state, zip):
        # Instance variables
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_id = student_id
        self.__phone = phone
        self.__email = email
        self.__street_address = street_address
        self.__city = city
        self.__state = state
        self.__zip = zip
     
        

    # Getter and Setters. 
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

    def set_first_name(self, value):
        self.__first_name = value
    
    def set_last_name(self, value):
        self.__last_name = value

    def set_student_id(self, value):
        self.__student_id = value
    
    def set_grade_level(self, value):
        self.__grade_level = value

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

    # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))
    
    # Method to print basic info about the student  
    def print_info(self):
        print(f"{self.__first_name} {self.__last_name} info:")
        print(f"email: {self.__email}   Phone: {self.__phone}")
        print(f"Address: {self.__street_address}, {self.__city}, {self.__state} {self.__zip}")
        
    def save_to_file(self):
        """Save student information for current object to file appended"""  
        # open  our file
        with open('final_project/students.txt', 'a') as file:
            # 🔚Please note you have to put in a new line symbol "\n" to end the line
            file.write(f"{self.__first_name}, {self.__last_name}, {self.__email}, {self.__phone}, {self.__street_address}, {self.__city}, {self.__state}, {self.__zip}\n")
            file.close()

    def mailing(self):
        """All mailing labels"""

    def tuition_reminder(self):
        """Create bill"""

class Section:
    """ contains section information: course name, number, section, subject,
        building, room, days, and time. """
    def __init__(self, subject, number, section, course_name,
                 description, dates, times, instructor, building, room):
        self.__course_name = course_name
        self.__number = number
        self.__section = section
        self.__subject = subject
        self.__building = building
        self.__room = room
        self.__days = days
        self.__time = time

    # Getter and Setter for first_name
    def get_course_name(self):
        return self.__course_name
    
    def get_number(self):
        return self.__number
    
    def get_section(self):
        return self.__section
    
    def get_subject(self):
        return self.__subject
    
    def get_building(self):
        return self.__building

    def get_room(self):
        return self.__room

    def get_days(self):
        return self.__days

    def get_time(self):
        return self.__time
    
    def set_course_name(self, value):
        self.__course_name = value

    def set_number(self, value):
        self.__number = value

    def set_section(self, value):
        self.__section = value

    def set_subject(self, value):
        self.__subject = value
    
    def set_building(self, value):
        self.__building = value

    def set_room(self, value):
        self.__room = value

    def set_days(self, value):
        self.__days = value

    def set_time(self, value):
        self.__time = value
    
        # Method to print basic info about the section
    def print_info(self):
        print(f"{self.__subject} {self.__number}-{self.__section}: {self.__course_name} ")
        print(f"Location: {self.__building} Room: {self.__room}")
        print(f"Days: {self.__days} Time: {self.__time}")
        
        
    

def directions():
    """ print a welcome message with directions on screen"""

def student_info():
    """ ✍🏽 Get student info, create an object with it, and write to file"""
    # pass information into class student
    # get input from the student - commented needed variables
    #     self.__first_name = first_name
    #     self.__last_name = last_name
    #     self.__student_id = student_id
    #     self.__phone = phone
    #     self.__email = email
    #     self.__street_address = street_address
    #     self.__city = city
    #     self.__state = state
    #     self.__zip = zip

    print("We need to get some basic information to register you for class.")
    fname = input("Please enter your first name:  ")
    lname = input("Please enter your last name:  ")
    id = int(input("Please enter your ID:  "))
    phone = input("Please enter your phone number with hyphens (815-555-555):  ")
    email = input("Please enter your email address:  ")
    street = input("Please enter your street address:  ")
    city = input("Please enter your city:  ")
    state = input("Please enter your state:  ")
    zip = input("Please enter your zip ")

    my_student = Student(fname, lname, id, phone, email, street, city, state, zip)
    #  my_student.print_info()
    my_student.save_to_file()


def display_classes():
    """ load available course sections from file, create an object for each one """
    # 📖 file final_project/read
    # 🐍 note from meri
    sections = []
    with open("final_project/schedule.txt", "r") as file:
        for line in file:
            # 🐞print(line)
            data = line.strip().split(",")
           
            
            # Assign each column to a variable
            subject = data[0]
            number = data[1]
            section = data[2]
            course_name = data[3]
            times = data[6]
            instructor = data[7]
            building = data[8]
            room = data[9]

        obj = sections(course_name=course_name,
                course_name=course_name,
                number=number,
                section=section,
                subject=subject,
                building=building,
                room=room,
                days=days,
                time=times,
                instructor=instructor
            )
        print(obj.print_info())



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

    class1 = Section("Programming Logic", "100", "001", "ADD", "G", "204", "TTh", "10:00-11:50  ")
    class1.print_info()


main()