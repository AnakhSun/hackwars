def test(s, name):
    s = s.replace(" ", "").lower()
    for letter in name.lower():
        flag = 0    
        for i in range(len(s.replace(" ", ""))):
            if letter == s.replace(" ", "").lower()[i]:
                s = s[i+1:]
                name = name[1:]
                flag = 1
                break
        if len(name) == 0:
            return True
        if flag == 0:
            return False


print(test("ppipip","Pippi"))