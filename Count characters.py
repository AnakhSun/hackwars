def count(str):
    answer ={}
    for char in str:
        if char in answer:
            answer[char] += 1
        if char not in answer:
            answer[char] = 1
    return answer

print(count("aabb"))