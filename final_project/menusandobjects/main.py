"""
main.py
-------
Main program for the Final Project (simplified and heavily commented).

This version matches the simplified schedule.txt file:
subject,number,section,course_name,building,room,days,time
"""

# 🌍 GLOBAL DICTIONARY: Department Abbreviation → Full Title
DEPARTMENTS = {
    "CDM": "Computers and Digital Media",
    "CSC": "Computer Science",
    "ADD": "Software Application Design and Development",
    "BUS": "Business",
    "ANI": "Animation"
}

from Student import Student
from Section import Section


# ----------------------------------------------------------------------
# 🪺 WELCOME MESSAGE
# ----------------------------------------------------------------------
def directions():
    print("Welcome to MCC Registration!")
    print("We will collect your information and create your account.\n")


# ----------------------------------------------------------------------
# 📁 FILE HELPERS FOR students.txt
# ----------------------------------------------------------------------
def load_students():
    """Reads students.txt and returns a list of records."""
    students = []

    with open("final_project/menusandobjects/students.txt") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            data = [item.strip() for item in line.split(",")]
            students.append(data)

    return students


def save_all_students(students):
    """💾 OVERWRITE students.txt with the UPDATED list."""
    with open("final_project/menusandobjects/students.txt", "w") as f:
        for row in students:
            f.write(",".join(row) + "\n")


# ----------------------------------------------------------------------
# 👩🏻‍🎓 COLLECT NEW STUDENT INFO
# ----------------------------------------------------------------------
def student_info():
    print("\n--- Enter Your Information ---")

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

    # 💾 Save new student to file
    stu.save_to_file()

    print("\nStudent information recorded.\n")
    return stu  # return full student object


# ----------------------------------------------------------------------
# 🔍 VERIFY / UPDATE STUDENT INFO
# ----------------------------------------------------------------------
def verify_info(stu):
    """
    Given a Student object, verify their information
    and allow edits using setter methods.
    """

    print("\n--- Verify Your Information ---")
    stu.print_info()

    while True:
        answer = input("Is everything correct? (y/n): ").strip().lower()

        if answer == "y":
            print("\nGreat! Moving forward...\n")
            return stu
        elif answer != "n":
            print("Please enter y or n.")
            continue

        # User wants to update info
        print("\nWhat would you like to change?")
        stu.print_info_numbered()

        try:
            choice = int(input("Enter the number to change: "))
        except ValueError:
            print("Invalid number.")
            continue

        new_val = input("Enter new value: ")

        # Apply update
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
            continue

        print("\nInformation updated!\n")
        stu.print_info()


# ----------------------------------------------------------------------
# 📚 DISPLAY CLASSES (Grouped by Subject)
# ----------------------------------------------------------------------
def display_classes():
    """
    Loads schedule.txt → creates Section objects → prints them GROUPED BY SUBJECT.
    Uses DEPARTMENTS to convert subject abbreviations to full titles.
    """

    section_list = []

    with open("final_project/menusandobjects/schedule.txt") as sfile:
        for line in sfile:
            line = line.strip()
            if line == "":
                continue

            data = line.split(",")

            if len(data) < 8:
                print("Skipping malformed line:", data)
                continue

            subj, number, sec, title, building, room, days, time = data
            obj = Section(title, number, sec, subj, building, room, days, time)
            section_list.append(obj)

    # 🔤 Sort by subject, then by course number
    section_list.sort(key=lambda s: (s.get_subject(), s.get_number()))

    print("\n📅 --- MCC COURSE SCHEDULE ---\n")

    index = 0
    previous_subject = ""

    while index < len(section_list):

        sec = section_list[index]
        subj = sec.get_subject()

        # 🎨 NEW SUBJECT HEADER
        if subj != previous_subject:
            previous_subject = subj
            full_title = DEPARTMENTS.get(subj, subj)

            print()
            print(f"🏷️  {full_title}")
            print("-" * len(full_title))

        # 🖨️ Print class info
        sec.print_info()
        print()

        index += 1


# ----------------------------------------------------------------------
# 🧾 SELECT CLASSES
# ----------------------------------------------------------------------
def select_classes(stu):
    """
    Allows the student to select one or more classes by entering:
        • Department (CSC)
        • Course Number (121)
        • Section Number (001)

    Builds a list of strings to send to billing().
    """

    print("\n📘 --- CLASS REGISTRATION ---\n")

    selected_classes = []   # holds invoice display lines
    keep_going = True       # loop flag

    while keep_going:

        dept = input("Enter Department (e.g., CSC): ").strip().upper()
        number = input("Enter Course Number (e.g., 121): ").strip()
        section = input("Enter Section (e.g., 001): ").strip()

        found = False

        with open("final_project/menusandobjects/schedule.txt") as sfile:
            for line in sfile:
                line = line.strip()
                if line == "":
                    continue

                data = line.split(",")

                if len(data) < 8:
                    continue

                subj, num, sec, title, building, room, days, time = data

                if subj == dept and num == number and sec == section:
                    found = True

                    # Calculate costs
                    tuition = 3 * 100
                    online_fee = 7 if (days == "Flexible Online" or time == "Flexible Online") else 0
                    total = tuition + online_fee

                    fee_text = " + $7 online" if online_fee > 0 else ""
                    invoice_line = f"{subj} {num}-{sec}  {title}  ${total}{fee_text}"

                    selected_classes.append(invoice_line)

                    print(f"\n✅ Registered for {subj} {num}-{sec}: {title}")
                    print(f"   Cost: ${total}{fee_text}\n")

                    break

        if not found:
            print("\n❌ Class not found. Try again.\n")
            select_classes(stu)

        again = input("Register for another class? (y/n): ").strip().lower()
        if again != "y":
            keep_going = False

    billing(stu, selected_classes)
    


# ----------------------------------------------------------------------
# 🧮 BILLING — Create Invoice
# ----------------------------------------------------------------------
def billing(stu, class_list):
    """
    Creates a text invoice in invoice_<studentID>.txt.
    Includes:
        • Student name & ID
        • All registered classes
        • Total amount due
    """

    print("\n🧮 --- BILLING & INVOICE GENERATION ---\n")

    total_due = 0

    for line in class_list:
        parts = line.split("$")
        if len(parts) > 1:
            amount = parts[1]
            amount = amount.replace("+ $7 online", "").strip()
            try:
                total_due += int(amount)
            except:
                pass

    # Build invoice text
    invoice_lines = []
    invoice_lines.append("MCC Course Registration Invoice\n")
    invoice_lines.append(f"Student: {stu.get_first_name()} {stu.get_last_name()}\n")
    invoice_lines.append(f"ID: {stu.get_student_id()}\n\n")
    invoice_lines.append("Registered Classes:\n")
    invoice_lines.append("-------------------\n")

    for item in class_list:
        invoice_lines.append(item + "\n")

    invoice_lines.append("\n-------------------\n")
    invoice_lines.append(f"Total Due: ${total_due}\n")

    # Save file
    filename = f"invoice_{stu.get_student_id()}.txt"
    path = f"final_project/menusandobjects/{filename}"

    with open(path, "w") as f:
        f.writelines(invoice_lines)

    print(f"💾 Invoice saved as {filename}\n")
    


# ----------------------------------------------------------------------
# 🚀 MAIN PROGRAM
# ----------------------------------------------------------------------
def main():
    directions()
    stu = student_info()
    verify_info(stu)
 
    display_classes()        # ← this now shows BEFORE class selection
    select_classes(stu)      # ← after seeing classes, user picks theirs


main()
