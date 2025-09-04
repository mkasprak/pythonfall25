# Define variables for centimeter values
cm_value_1 = 25.4
cm_value_2 = 50.8
cm_value_3 = 76.2
cm_value_4 = 101.6

# Conversion factor: 1 inch = 2.54 centimeters
conversion_factor = 2.54

# Calculate inches for each centimeter value
inches_1 = cm_value_1 / conversion_factor
inches_2 = cm_value_2 / conversion_factor
inches_3 = cm_value_3 / conversion_factor
inches_4 = cm_value_4 / conversion_factor

# Output the results
print(f"{cm_value_1} centimeters is equal to {inches_1:.2f} inches.")
print(f"{cm_value_2} centimeters is equal to {inches_2:.2f} inches.")
print(f"{cm_value_3} centimeters is equal to {inches_3:.2f} inches.")
print(f"{cm_value_4} centimeters is equal to {inches_4:.2f} inches.")