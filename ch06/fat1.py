def fat1(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print(fat1(3))
print(fat1(5))