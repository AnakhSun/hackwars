def expanded_form(num):
    answer = ""
    op = len(str(num))
    for i in range(op-1, -1, -1):
        temp_num = str(num//pow(10, i)*pow(10, i))
        num -= num//pow(10, i)*pow(10, i)
        if temp_num != "0":
            answer += temp_num
        if num != 0 and i != 0 and temp_num != "0":
            answer += " + "
    return answer


print(expanded_form(866860))