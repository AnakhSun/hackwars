def order(sentence):
    words = sentence.split()
    nums = [f"{i}" for i in range(1, 10)]
    answer = ["" for _ in range(0, len(words))]
    for word in words:
        for num in nums:
            if num in word:
                i = int(num)
        answer[i-1] = word
    s = ""
    for a in answer:
        s += a + " "
    return s[:-1]

print(order("4of Fo1r pe6ople g3ood th5e the2"))