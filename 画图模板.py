## 画三维图
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
figure = plt.figure()
ax = Axes3D(figure)
X = np.arange(0, 1, 0.05)
Y = np.arange(0, 1, 0.05)
#网格化数据
X, Y = np.meshgrid(X, Y)
R = 2 * X * Y / (X + Y)
ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap='rainbow')

plt.show()


## 画二维图
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
figure = plt.figure()
X = np.arange(-10, 10, 0.25)
R = np.exp(X) / (1 + np.exp(X))
plt.plot(X, R)
plt.show()