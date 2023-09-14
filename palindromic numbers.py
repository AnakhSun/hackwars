
def palindromize(number):
    if number != 196:
        number = str(number)
        flag = 0
        iterations  = 0
        while flag == 0:
            flag = 1
            if len(number) % 2 == 1:
                n = (len(number) - 1) // 2
                for i in range(0, n):
                    if number[i] != number[n*2-i]:
                        flag = 0
                        iterations += 1
                        break

            if len(number) % 2 == 0:
                n = (len(number)) // 2
                for i in range(0, n):
                    if number[i] != number[n*2-i-1]:
                        flag = 0
                        iterations += 1
                        break
            
            if flag == 1:
                res = int(number)
            number = str(int(str(number)) + int(str(number)[::-1]))

        return str(iterations) + " " + str(res)
    else:
        return None
       
print(palindromize(195))