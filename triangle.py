"""
    Demonstrating an area function
"""


# Rectangle function will accept two variables, calculate, and display the area of a rectangle
def rectangle(length, width):
    area = length * width
    print(f"The area of a rectangle with a length of {length} and a width of {width} is: {area: ,.2f}")


rectangle(10, 5)