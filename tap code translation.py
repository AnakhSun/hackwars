def tap_code_translation(word):
    key = [
        ["a", "b", "c", "d", "e"],
        ["f", "g", "h", "i", "j"],
        ["l", "m", "n", "o", "p"],
        ["q", "r", "s", "t", "u"],
        ["v", "w", "x", "y", "z"]
        ]


    word = word.replace("k", "c")
    answer = ""
    for char in word:
        for i in range(len(key)):
            for j in range(len(key[0])):
                if char == key[i][j]:
                    answer += "." * (i+1) + " " + "." * (j+1) + " "
                    break

    return(answer[:-1])   
       
print(tap_code_translation("taps"))                
