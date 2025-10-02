"""

    dictionary demo
"""

numbers_japanese = {
    1: "ichi",
    2: "ni",
    3: "san",
    4: "yon",   # (also "shi", but yon is safer/neutral)
    5: "go",
    6: "roku",
    7: "nana",  # (also "shichi", but nana is safer/neutral)
    8: "hachi",
    9: "kyuu",  # (also "ku")
    10: "juu",
    11: "juu-ichi",
    12: "juu-ni",
    13: "juu-san",
    14: "juu-yon",
    15: "juu-go",
    16: "juu-roku",
    17: "juu-nana",
    18: "juu-hachi",
    19: "juu-kyuu",
    20: "ni-juu"
}


# using keys 
# for i in range(1,21):
#     number = numbers_japanese[i]
#     print(number)



value = numbers_japanese.get(0, "rei")
print(value)

for key in numbers_japanese:
    print(key, numbers_japanese[key])

for key, value in numbers_japanese.items():
    if key > 10:
     print(key, value)