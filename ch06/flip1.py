def flip(some_list):
#    return some_list[::-1]
    if len(some_list) < 2:
        return some_list
    else:
        return flip(some_list[1:]) +some_list[:1]
# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)