def solution(number):
    sum = 0
    while number > 0:
        number -=1
        if number % 3 == 0 or number % 5 == 0:
            sum += number   
    return sum

print(solution(1000))
  