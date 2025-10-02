"""

    dictionary and error checking with exceptions


"""

SECRET_CODE = {
    "a": "🍎",
    "b": "🐝",
    "c": "🌊",
    "d": "🐬",
    "e": "🥚",
    "f": "🐸",
    "g": "🦒",
    "h": "🏠",
    "i": "🍦",
    "j": "🕹️",
    "k": "🔑",
    "l": "🦁",
    "m": "🌙",
    "n": "🎶",
    "o": "🐙",
    "p": "🥞",
    "q": "👑",
    "r": "🌈",
    "s": "⭐",
    "t": "🌴",
    "u": "☂️",
    "v": "🎻",
    "w": "🌍",
    "x": "❌",
    "y": "🧶",
    "z": "🦓",
    " ": "⬜",   # space
    ",": "⚓",
    "!": "💥",
    ".": "🔵"
}


def create_code(word):
    # using get in case does not exist
    code = ""
    word = word.lower()
    for letter in word:
        symbol = SECRET_CODE.get(letter, "⁉️")
       # print(symbol)
        code = code + symbol
    return code

def decode(code):
    result = ""
    for symbol in code:
        for k, v in SECRET_CODE.items():
            if v == symbol: 
                result += k

    return result



def main():
    try:
        value = 0
        print(" 1. Create Secret Code \n 2. Decode \n 3. Quit")
        while value > 3 or value < 1:
            value = int(input("Please enter a number for your selection (1, 2 or 3 to quit):") )
            if value == 1:
                my_word = input("Please enter a word or phrase:   ")
                result = create_code(my_word)
            elif value == 2:
                my_code = input("Paste the code!:  ")
                result = decode(my_code)
            elif value == 3: 
                break

            print(result)
            value = 0
    except UnboundLocalError:
        print("I'm sorry, you need to enter a number between 1 and 3")
        
    except ValueError:
        print("I'm sorry, that is not a number")
      

main()