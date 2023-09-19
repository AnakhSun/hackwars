def sum_dig_pow(a, b):
    answer = []
    for num in range(a, b+1):
        num_str = str(num)
        i = 1
        control_num = 0
        for char in num_str:
            control_num += pow(int(char), i)
            i+=1
        if control_num == num:
            answer.append(num)
    return answer


print(sum_dig_pow(89, 135))