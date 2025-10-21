""" programming the song bingo  👏"""

def print_verse(bingo_name):
    """
        print the structure of the song verse with a given dog name
    """

    print("There was a farmer who had a dog")
    print(f"And {bingo_name} was his nameo")
    for _ in range(3):
        for letter in bingo_name:
            print(letter.upper(), end=" ")
        print()


def main():
    """
        set up variables, run loop for chorus, replace values
    """
    dog = list("Bingo")  # Initialize the dog's name as a list for character replacement
    replacement_index = len(dog) - 1  # Start replacing from the last letter


      # Loop over each verse of the song
    for _ in range(len(dog) + 1):  # +1 to include the fully replaced name
        bingo = ''.join(dog)  # Join the list to a string for current verse
        print_verse(bingo)  # Print the verse with current name format


         # Replace one letter with emoji for the next verse, if not all replaced
        if replacement_index >= 0:
            dog[replacement_index] = "👏"
            replacement_index -= 1
main()