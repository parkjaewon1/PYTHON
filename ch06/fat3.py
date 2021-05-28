def fat1(num):
    result = 1
    # 1*2*3 => 3 * 2 * 1 = 6
    # 1*2*3*4*5 => 5 * 4 * 3 * 2 * 1 = 120
    for i in range(num, 1, -1): # num부터 2까지 1씩 빼서 I에 대입
        print(i,'* ',end='')
        result *= i
    print('1 = ', end='')
    return result

print(fat1(3))
print(fat1(5))
 