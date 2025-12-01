"""
main.py
-------
Main program for the Final Project (simplified and heavily commented).

This version now matches the simplified sections.txt file:
subject,number,section,course_name,building,room,days,time
"""

from Student import Student
from Section import Section


# ----------------------------------------------------------------------
# 🪿 WELCOME
# ----------------------------------------------------------------------
def directions():
    print("Welcome to MCC Registration!")
    print("We will collect your information and create your account.\n")


# ----------------------------------------------------------------------
# 🐥 FILE HELPERS FOR STUDENTS.TXT
# ----------------------------------------------------------------------
def load_students():
    students = []

    with open("final_project/menusandobjects/students.txt") as file:
        # 🔎 NOTE:
        # 🐍 Python automatically closes the file when the "with" block ends.
        for line in file:
            line = line.strip()

            # ⚠️ WARNING:
            # A blank line at the end of the file will break split().
            if line == "":
                continue

            data = line.split(",")
            students.append(data)

    return students


def save_all_students(students):
    """
    💾 FILE:
    Overwrites students.txt with the UPDATED list of all student records.
    """
    with open("final_project/menusandobjects/students.txt", "w") as f:
        for row in students:
            # 🔎 NOTE: Join list → CSV-style string → add newline
            f.write(", ".join(row) + "\n")


# ----------------------------------------------------------------------
# 👩🏻‍🎓 COLLECT STUDENT INFO
# ----------------------------------------------------------------------
def student_info():
    print("\n--- Enter Your Information ---")

    # 🧪 CHECKPOINT:
    # All user input belongs in main.py
    fname = input("First name: ")
    lname = input("Last name: ")
    sid = int(input("Student ID: "))
    phone = input("Phone (###-###-####): ")
    email = input("Email: ")
    street = input("Street Address: ")
    city = input("City: ")
    state = input("State: ")
    zip_code = input("Zip Code: ")

    stu = Student(fname, lname, sid, phone, email, street, city, state, zip_code)

    # 💾 FILE:
    # save_to_file() uses APPEND mode → adds a new line at bottom.
    stu.save_to_file()

    print("\nStudent information recorded.\n")

    verify_info(sid)


# ----------------------------------------------------------------------
# ⁉️ VERIFY / UPDATE STUDENT INFO
# ----------------------------------------------------------------------
def verify_info(sid):
    students = load_students()

    index = 0  # 📌 INFO: replacing enumerate() since not taught yet
    while index < len(students):

        row = students[index]

        if int(row[2]) == sid:
            # 📚 LEARNING MOMENT:
            # Rebuild the Student object using stored file data.
            stu = Student(row[0], row[1], int(row[2]),
                          row[4], row[3], row[5],
                          row[6], row[7], row[8])

            print("\n--- Verify Your Information ---")
            stu.print_info()

            correct = input("Is everything correct? (y/n): ")

            if correct.lower() == "y":
                print("\nGreat! Now we can select classes.\n")
                select_classes(sid)
                return

            print("\nWhat would you like to change?")
            stu.print_info_numbered()

            choice = int(input("Enter the number to change: "))
            new_val = input("Enter new value: ")

            # 📚 LEARNING MOMENT:
            # Using the setter methods.
            if choice == 1: stu.set_first_name(new_val)
            elif choice == 2: stu.set_last_name(new_val)
            elif choice == 3: stu.set_email(new_val)
            elif choice == 4: stu.set_phone(new_val)
            elif choice == 5: stu.set_street_address(new_val)
            elif choice == 6: stu.set_city(new_val)
            elif choice == 7: stu.set_state(new_val)
            elif choice == 8: stu.set_zip(new_val)
            else:
                print("Invalid choice.")
                return

            # 💾 FILE:
            # Convert updated object back into list form
            students[index] = [
                stu.get_first_name(),
                stu.get_last_name(),
                str(stu.get_student_id()),
                stu.get_email(),
                stu.get_phone(),
                stu.get_street_address(),
                stu.get_city(),
                stu.get_state(),
                stu.get_zip()
            ]

            # 🔎 NOTE: Sort by student ID using a tiny one-time lambda function
            students.sort(key=lambda x: int(x[2]))

            save_all_students(students)
            print("\nInformation updated!\n")
            return

        index += 1


# ----------------------------------------------------------------------
# 👁️ DISPLAY CLASSES 
# ----------------------------------------------------------------------
def display_classes():
    """
    Loads sections.txt, creates Section objects,
    and displays them GROUPED BY SUBJECT using a while loop.

    NEW FILE FORMAT (8 fields):
        subject,number,section,course_name,building,room,days,time
    """

    section_list = []

    with open("final_project/menusandobjects/sections.txt") as sfile:
        for line in sfile:
            line = line.strip()

            # ⚠️ WARNING: Skip blank lines so our program doesn't crash
            if line == "":
                continue

            data = line.split(",")

            # ⚠️ WARNING: Safety check for incomplete rows
            if len(data) < 8:
                print("Skipping malformed line:", data)
                continue

            subj = data[0]
            number = data[1]
            sec = data[2]
            title = data[3]
            building = data[4]
            room = data[5]
            days = data[6]
            time = data[7]

            # 📌 INFO: Create a Section object for each row
            obj = Section(title, number, sec, subj, building, room, days, time)
            section_list.append(obj)

    # 🔎 NOTE: Sorting first by subject, then by number
    section_list.sort(key=lambda s: (s.get_subject(), s.get_number()))

    print("\n--- MCC COURSE SCHEDULE ---\n")

    index = 0
    previous_subject = ""

    # 📌 INFO: Grouping using a while loop (NOT for...in)
    while index < len(section_list):
        sec = section_list[index]
        subj = sec.get_subject()

        # NEW SUBJECT GROUP?
        if subj != previous_subject:
            previous_subject = subj
            print()
            print(subj.upper())
            print("-" * len(subj))

        sec.print_info()
        print()

        index += 1


# ----------------------------------------------------------------------
# PLACEHOLDERS
# ----------------------------------------------------------------------
def select_classes(sid):
    """🛠️ TODO: We will build a class-selection menu together in class."""
    pass


def billing():
    """🛠️ TODO: Students will design their billing function in class."""
    pass


# ----------------------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------------------
def main():
    directions()
    student_info()
    display_classes()
    billing()


main()
