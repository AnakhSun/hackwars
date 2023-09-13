def check(sentence, name):
    letters = {}

    for l in "qwertyuiopasdfghjklzxcvbnm1234567890":
        letters[l] = 0


    for letter in sentence.replace(" ", "").lower():
        letters[letter] += 1
        pass
    
    for letter in name.replace(" ", "").lower():        
        if letters[letter] == 0: 
            return False
        if letters[letter] > 0:
            letters[letter] -= 1
    return True

def test(s, name):
    s = s.replace(" ", "").lower()
    for letter in name.lower():
        flag = 0    
        for i in range(len(s.replace(" ", ""))):
            if letter == s.replace(" ", "").lower()[i]:
                s = s[i+1:]
                name = name[1:]
                flag = 1
                print(s)
                print(name)
                print("----------")
                break
        if len(name) == 0:
            return True
        if flag == 0:
            return False


print(test("ppipip","Pippi"))