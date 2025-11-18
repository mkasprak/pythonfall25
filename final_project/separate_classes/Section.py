"""
section.py
----------
Defines the Section class used for representing course sections.

Students Will Modify:
    • Add additional details (instructor, seats available, credits, etc.)
    • Improve output formatting.
    • Connect to file-based loading in main.py later in the project.
"""

class Section:
    """
    Represents one class section, including schedule and room information.
    """

    def __init__(self, course_name, number, section,
                 subject="ADD", building=None, room=None,
                 days=None, time=None):
        self.__course_name = course_name
        self.__number = number
        self.__section = section
        self.__subject = subject
        self.__building = building
        self.__room = room
        self.__days = days
        self.__time = time

    # Getters
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

    # Setters
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

    # Display
    def print_info(self):
        """Print formatted class section information."""
        print(f"{self.__subject} {self.__number}-{self.__section}: "
              f"{self.__course_name}")
        print(f"Location: {self.__building} Room: {self.__room}")
        print(f"Days: {self.__days}   Time: {self.__time}")
