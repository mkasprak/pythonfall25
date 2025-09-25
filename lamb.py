"""
    Returning values from functions
"""

def setup():
    print("                                  Mad Libs!")
    print("Please enter the type of word you are asked for, then I will tell you a story.")


def get_words():
    name = input("Please enter a name:  ")
    size = input("Please enter a size (sm, med, lrg, etc.):  ")
    animal = input("Please enter a kind of animal:  ")
    color = input("Please enter a color:  ")

    story(name, size, animal, color)

def story(name_in, size_in, animal_in, color_in):
    print(f"{name_in} had a {size_in} {animal_in}")
    print(f"{size_in} {animal_in}")
    print(f"{size_in} {animal_in}")
    print(f"<mark>Whose fleece was {color_in} as snow</mark>")

    print("Original poem by Sarah Josepha Hale")

def main():
    setup()
    get_words()


main()