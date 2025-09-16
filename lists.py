"""
    Working with lists
"""


favorite_things = ["kayak", "computer", "custom keyboard", "matcha latte", "bicycle"]

# print(favorite_things)


# append

# favorite_things.append("Dogs")


# remove (by value NOT index)

favorite_things.remove("kayak")

# sort
favorite_things.sort()

#favorite_things.reverse()


print(len(favorite_things))


three = favorite_things.pop(3)

print(three)