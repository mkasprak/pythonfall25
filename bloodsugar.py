
"""
    Gather a user's blood sugar for a day in a multi level list
    Print the times and the blood sugar on the screen
    calculate and print the average blood sugar
"""

# variables
blood_sugar_times = ["Before Breakfast",
                     "Before Lunch", "Before Dinner", "Before Bed"]
total = 0

blood_sugar_with_times = []
# get info from user
for time in blood_sugar_times:
    sugar_level = int(input(f"Please enter the {time} blood sugar level: "))
    while sugar_level > 400 or sugar_level < 60:
        correct_number = input(
            f"The level {sugar_level} is outside of normal ranges. Are you sure? (Y or N)")
        if correct_number == "Y" or correct_number == "y":
            break
        else:
            sugar_level = int(input(f"Please enter the {time} blood sugar level: "))
    blood_sugar_with_times.append([time, sugar_level])

# print results to screen
for item in range(len(blood_sugar_with_times)):
    print(f"For {blood_sugar_with_times[item][0]} the blood sugar was {blood_sugar_with_times[item][1]}")
    total += blood_sugar_with_times[item][1]

average = total / len(blood_sugar_with_times)
print(f"Your average blood sugar today was: {average:.1f}")