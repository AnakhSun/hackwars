def presses(phrase):
    phrase = phrase.lower()
    keyboard = {"1": ["1"],
                "2": ["a", "b", "c", "2"],
                "3": ["d", "e", "f", "3"],
                "4": ["g", "h", "i", "4"],
                "5": ["j", "k", "l", "5"],
                "6": ["m", "n", "o", "6"],
                "7": ["p", "q", "r", "s", "7"],
                "8": ["t", "u", "v", "8"],
                "9": ["w", "x", "y", "z", "9"],
                "*": ["*"],
                "0": [" ", "0"],
                "#": ["#"]}

    sum = 0
    for char in phrase:
        for key, simbols in keyboard.items():
            if char in simbols:
                for i in range(len(simbols)):
                    if char == simbols[i]:
                        sum += i+1
                        break
    return sum  
                  
print(presses("lol"))