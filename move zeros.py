def move_zeros(lst):
    answer = [0 for _ in range(len(lst))]
    index = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            answer[index] = lst[i]
            index += 1
    return answer



print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))