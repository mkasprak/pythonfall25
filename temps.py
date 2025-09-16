"""
    Averag temp

"""


months=["January", "February", "March"]
temp=[] # empty list
total = 0
for month in months:
    average_temp = int(input(f"Please enter the average temperature for {month}: "))
    temp.append(average_temp)

for my_temp in temp:
    print(my_temp)
    total = total + my_temp
    print(f"total: {total}")

print(f"The average temperature was: {total / len(temp): .2f}")