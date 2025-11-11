"""
    letting people order off of a drive through menu, print reciept,
    read in menu  from text file

"""
class drivethrough_menu:
    def __init__(self, item_name, item_price):
        self.__item_name = item_name
        self.__item_price = item_price

""" on thursday"""

class customer_order:
    def __init__(self, customer_number, items): 
        # items will be a list (multi level, item and  price)
        self.__customer_number = customer_number
        self.__items





menu= [["blank", 0], ["Hamburger", 1.0], ["Soda", 1.5], ["Fries", 1.0]]



def initialize_menu():
    """init """
    print("1. Hamburger    $1.00")
    print("2. Soda         $1.50")
    print("3. Fries        $1.00")
def ask_for_choice():
    """ choice """
    choice = 1
    order = []
    while choice != 0:
        print("Enter 0 when you are done.")
        my_choice = int(input(f"Please enter the number of the item you want."))
        order.append(menu[my_choice])

    with open("final/order.txt", "a") as file:
        file.write 
    

def take_orders_until_done():
    """will call choice"""

def calculate_total():
    """ calculate """

def display_order():
    """ display """
    

def display_total():
    """ displya total"""






def main():
    """Organze calling functions and main logic """
    initialize_menu()

main()