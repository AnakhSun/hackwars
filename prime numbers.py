def is_prime(num):
    n = round(num/2)
    if num <= 1:
        return False
    for i in range(2, n+1):
        if num % i == 0:
            return False
    return True

print(is_prime(75))