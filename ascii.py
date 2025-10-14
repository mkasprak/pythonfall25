"""
    Demonstrate looking up ASCII values
    Meaningfully use try and expcept

"""



def main():
    try:
        char = input("Please enter a single character:  ")
        while len(char) != 1:
            print("I'm sorry, I can only work with single characters")
            char = input("Please enter a single character:  ") 
        ascii_value = ord(char)
        print(f"The asciii value of {char} is {ascii_value}")
    except Exception as e:
        print(e)



main()