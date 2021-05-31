import ch07.cal
# ch07.cal에서 plus, multiply를 사용
# from ch07.cal import plus, multiply
from ch07.cal import * # *는 모두, 권장하지 않음
import ch07.cal as c # ch07.cal을 별칭 c
from ch07.cal import multiply as m
print(ch07.cal.plus(12, 6))
print(ch07.cal.multiply(12, 6))
print(divide(12,5))
print(plus(1,5))
print(multiply(2,3))
print(c.minus(12, 7))
print(c.divide(12, 5))
print(m(3,4))