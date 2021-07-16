import numpy as np
#                  평균 표준편차 차원
a = np.random.normal(0, 1, (2,3))
print(a)
data = np.random.normal(0, 1, 10000)
import matplotlib.pylab as plt
plt.hist(data, bins=100)
plt.show()