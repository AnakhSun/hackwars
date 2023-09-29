def encode(string):
    answer = ""
    for char in string:
        answer += " "     
        for i in range(0, len(keys)):
            for j in range(0, len(keys[i])):
                for k in range(0, len(keys[i][j])):
                    if char == keys[i][j][k]:
                        answer += "." * (k+1) + " " + "." * (j+1) + " " + "." * (i+1)
    return answer[1:]              


def decode(string):
    mass = string.split(" ")
    answer = ""
    for i in range(0, len(mass), 3):
        second = len(mass[i])-1
        first = len(mass[i+1])-1
        key = len(mass[i+2])-1
        answer += keys[key][first][second]        
    return answer

keys = [
        [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ],

        [
            ["J", "K", "L"],
            ["M", "N", "O"],
            ["P", "Q", "R"]
        ],
        
        [
            ["S", "T", "U"],
            ["V", "W", "X"],
            ["Y", "Z", " "]
        ]
]


print(decode(".. . ... .. .. . . . ... .. . ..."))