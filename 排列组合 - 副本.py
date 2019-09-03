# 求组合数

# 笔试时想出来的版本
def c(n, m):
    fenmu = 1
    fenzi = 1
    for i in range(n - m + 1, n + 1):
        fenmu *= i
    for j in range(1, m + 1):
        fenzi *= j
    return fenmu // fenzi


import math
# 用math库阶乘计算
def comb(n, m):
    return math.factorial(n) / (math.factorial(n - m) * math.factorial(m)) 


# 用自带库函数计算
from scipy.special import perm, comb

print(comb(4, 2))



## 求排列数
import math
def perm(n, m):
    return math.factorial(n) / math.factorial(n - m)
print(perm(4, 2))