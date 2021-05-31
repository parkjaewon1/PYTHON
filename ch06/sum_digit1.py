def sum_digits(n):
    if n < 10:
        return n
    else:              # 2 +     2 + 5  + 4 + 1
        str_n = str(n) # 22541 2541 541 41
    return int(str_n[0]) + sum_digits(int(str_n[1:]))
# 문자로 변경하지 말고 자릿수 합
def sum_digits2(n):
    if n < 10:
        return n # 1 + 4    + 5  + 2 + 2
    else: # 22541  2254 225   22   2
        return n % 10 + sum_digits2(n // 10)
# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))
print("==============")
print(sum_digits2(22541))
print(sum_digits2(92130))
print(sum_digits2(12634))
print(sum_digits2(704))
print(sum_digits2(3755))