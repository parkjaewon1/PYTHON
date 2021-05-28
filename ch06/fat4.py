def fat1(num):
    # fat1(3) : fat1(2) * 3 => fat1(1) * 2 * 3 => 1 * 2 * 3
    # fat2(5) : fat(4)*5=>fat(3)*4*5=>fat(2)*3*4*4=>fat1(1)*2*3*4*5=>1*2*3*4*5
    if num > 1:
        print(num,'* ',end='')
        return fat1(num - 1) * num
    else:
        print('1 = ',end='')
        return 1

print(fat1(3))
print(fat1(5))
