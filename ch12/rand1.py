import numpy as np
a = np.random.rand(3,2) # [0,1)의 3행 2열 0부터 1미만이 실수 균등분표 uniform distribution
print(a)
# data = np.random.rand(10000)
# data = np.random.randn(10000)  # n은 normal
#               정수     시작   끝  갯수
data = np.random.randint(-100, 100, 10000)
import matplotlib.pylab as plt
plt.hist(data, bins=10)
plt.show()