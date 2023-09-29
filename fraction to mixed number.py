import math

def mixed_fraction(s):
    f = ""
    c = 0
    for char in s:
        if char == "-":
            c += 1
    a = int(s.split("/")[0].replace("-", ""))
    b = int(s.split("/")[1].replace("-", ""))
    if c %  2 == 0:
        f = ""
    if c % 2 == 1:
        f = "-"
    answer = f
    if b == 0:
        raise ZeroDivisionError
    if a == 0:
        return '0'
    if a%b == 0:
        return answer + str(a//b)
    else:
        if a//b != 0:
            answer += str(a//b) + " "
        o = 1
        while o:
            i = 2
            while i <+ round(math.sqrt(a))+2:
            
                if b % i == 0 and a % i == 0:
                    
                    a = a // i
                    b = b // i
                    i = 2
                    continue
                i += 1
                o = 0
              
        answer += str(a%b) + "/" + str(b)
    return answer

print(mixed_fraction("1467312/-9037252"))