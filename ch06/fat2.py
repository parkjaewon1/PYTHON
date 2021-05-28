def fat1(num):
    if num > 1:
        return fat1(num - 1) * num
    else:
        return 1
print(fat1(3))
print(fat1(5))
        