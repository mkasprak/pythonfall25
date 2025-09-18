"""
    more lists
"""
high_temps_july: list[int] = [94, 91, 92, 92, 94, 88, 82, 85, 84, 84, 84, 81, 81, 84, 88, 88, 72, 77, 79, 73, 81, 84, 90, 91, 81, 81, 86, 86, 93, 91, 73]



for day in range (1, 32):
    print(f"On July {day} the high temp was:  {high_temps_july[day -1]}")

total = sum(high_temps_july)
num_days = len(high_temps_july)
average = total / num_days

print(f"The average daily high temp for July was: {average: ,.1f}")