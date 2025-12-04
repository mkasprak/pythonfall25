"""
section.py
----------
Defines the Section class used for representing class sections.

This version mirrors the documentation style found in main.py.
Students can refer to this file as a model for how classes store
multiple attributes and provide methods for formatted output.

File connects directly to:
    • schedule.txt  (loaded in main.py)
    • display_classes() function in main.py
"""

# ----------------------------------------------------------------------
# 🏫 SECTION CLASS — Represents one section of a course
# ----------------------------------------------------------------------
class Section:
    """
    Represents one class section, including:
        • subject abbreviation (e.g., CSC)
        • course number (string in file → may convert to int for sorting)
        • section number (001, 002, etc.)
        • course title
        • building, room
        • meeting days, meeting time
    """

    # ------------------------------------------------------------------
    # 🏗️ INITIALIZER
    # Creates a section object from one row of schedule.txt.
    # ------------------------------------------------------------------
    def __init__(self, course_name, number, section,
                 subject="ADD", building="", room="",
                 days="", time=""):

        self.__course_name = course_name
        self.__number = number            # stored as string from file
        self.__section = section
        self.__subject = subject
        self.__building = building
        self.__room = room
        self.__days = days
        self.__time = time

    # ------------------------------------------------------------------
    # 📥 GETTERS — used in display_classes() when grouping/sorting
    # ------------------------------------------------------------------
    def get_course_name(self): return self.__course_name

    def get_number(self):
        """
        Returns the course number as an integer if possible.
        This lets main.py sort sections numerically.
        """
        try:
            return int(self.__number)
        except:
            return self.__number

    def get_section(self): return self.__section
    def get_subject(self): return self.__subject
    def get_building(self): return self.__building
    def get_room(self): return self.__room
    def get_days(self): return self.__days
    def get_time(self): return self.__time

    # ------------------------------------------------------------------
    # ✏️ SETTERS — included for teaching purposes and future CRUD work
    # ------------------------------------------------------------------
    def set_course_name(self, v): self.__course_name = v
    def set_number(self, v): self.__number = v
    def set_section(self, v): self.__section = v
    def set_subject(self, v): self.__subject = v
    def set_building(self, v): self.__building = v
    def set_room(self, v): self.__room = v
    def set_days(self, v): self.__days = v
    def set_time(self, v): self.__time = v

    # ------------------------------------------------------------------
    # 🖨️ DISPLAY OUTPUT
    # Used in main.py inside display_classes().
    # ------------------------------------------------------------------
    def print_info(self):
        """Prints one formatted course section line."""
        print(f"{self.__subject} {self.__number}-{self.__section}: {self.__course_name}")
        print(f"Location: {self.__building} Room: {self.__room}")
        print(f"Days: {self.__days}  Time: {self.__time}")
