"""
    Creating and working with multiple exceptions
    Choose your own adventure.....

"""

def princess(name): 
    print(f"Once upon a time, there was a princess named {name}")
    # def calculate_discount(price, discount):
    #     assert 0 <= discount <= 100, "Discount must be between 0 and 100"
    #     return price * (100 - discount) / 100
    
    try:
        pet = input("Our princess had a pet, it was a: (enter animal)") 
        assert  pet.strip() != "" # not blank
        print(f"She loved her {pet} very much.")
    except AssertionError as err:
        print(f"🐶 We need an animal type!")
        princess(name)
    except Exception as e:
        print (f"You had an error {e}")
def knight(name):    
    print(f"Once upon a time, there was a Knight named {name}")

def main():
    # Get User information
    # Select a "chapter " function
    try:
        print("Creating a custom bedtime story! ")
        name = input("Hey there! I heare you would like me to tell you a story! \nWhat is your name:")
        storyline = int(input(f"Hello, {name}, would you like a story about a (1) princess or a (2) knight?")  )
        # if statement to select correct function;
        if storyline == 1:
            princess(name)
    
    except Exception as e:
        print(f"You had the error {e}")




main()