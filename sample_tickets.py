"""
    working with lists caller number 7 wins $110

"""

# generate

caller = [1,2,3,4,5,6,7,8,9,10 ]
# caller.remove(7)
# for call in caller:
#     if call != 7:
#         print(f"I'm sorry, you are caller number {call}")
#     else:
#         print(f"Congratulations, you win!!!!")


# guess a number
guess = 0
while guess <= 0 or guess > 10:
    guess = int(input("Pick a number between 1 & 10:  "))
    if guess< 1 or guess > 10:
        print(f"{guess} is invalid")

caller.remove(guess)
for call in caller:
    print(call)