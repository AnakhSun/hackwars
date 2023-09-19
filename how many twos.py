def two_count(n):
    res = 0
    while n % 2 == 0:
        res +=1
        n = n // 2
    return res

print(two_count(4))