""" 

    demonstrate global variables
"""

PI = 3.14 # global because outside of functions in scope everywhere



def main():
    global PI
    PI = 3.13149
    area = PI * (4 *4) 
    print(f"area is {area: ,.1f}")

main()