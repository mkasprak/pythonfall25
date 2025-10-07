"""
    This is where the directions go!
    Import Random,
    Generate a random number,
    generate a second random number,
    determine which one is larger - by how much
    uses the Random module
"""
import random


def generate():
    """
        called by main
        generates and returns a random number between 1 and 100
    """
    my_random = random.randint(1,100)
    return my_random








def main():
    """
        call generate function to return a random number between 1 and 100
        call again for second number
        determine (in main) which number is larger, and by how much
        display results on screen

    """
    # get random numbers
    num_1 = generate()
    #print(f"Numeber 1: {num_1}")
    num_2 = generate()
    #print(f"Numeber 2: {num_2}")

    # evaluate distance between them

    difference = abs(num_1 - num_2)
    print(f"The difference between the values is: {difference}")
    if num_1 > num_2:
        print(f"Number 1: {num_1} is larger than Number 2: {num_2}")
    else:
        print(f"Number 2: {num_2} is larger than Number 1: {num_1}")



main()