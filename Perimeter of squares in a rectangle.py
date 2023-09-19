def perimeter(n):
    array = [1, 1]
    if n == 1:
        return 4
    if n == 2:
        return 8
    for i in range(1, n):
        array.append(array[i-1]+array[i])
    res = sum(array)*4
    return res
    

print(perimeter(7))