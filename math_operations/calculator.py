"""
    Step 1: Creating a Python Module
Create a new file named calculator.py in a folder named modules.
Add the following code to calculator.py:
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
Step 2: Using the Module in Another Script
Create a file named main.py in the same folder and use the calculator module:
import calculator

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)
Step 3: Organizing Code into Packages
Create a folder named math_operations and move calculator.py into it.
Add an empty __init__.py file to the folder.
Update main.py to import the module from the package:
from math_operations import calculator

result = calculator.add(7, 2)
print("Result:", result)
Step 4: Adding More Modules
Create additional modules like geometry.py to calculate areas of shapes. This will help you understand how packages can grow to organize more functionality.


"""
def add(a, b):
    return a + b

def subtract(a,b):
    return a - b