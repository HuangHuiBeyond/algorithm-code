# # -*- coding: utf-8 -*- 
from matplotlib import pyplot as plt
import numpy as np


## 方法1：按照定义计算
'''
此函数可以计算阶梯状的auc，但是如果有样本的概率相等但是label不一样，会形成梯形，此时无法计算
'''
n = 10
arr = [[1, 0.9], [0, 0.7], [1, 0.6], [1, 0.55], [0, 0.52], [1, 0.4], [0, 0.38], [0, 0.35], [1, 0.31], [0, 0.1]]
def confuse(k):
    '''
    计算混淆矩阵，并输出假阳性率和真阳性率
    '''
    tp = 0 ## 真阳
    tn = 0 ## 真阴
    fp = 0 ## 假阳
    fn = 0 ## 假阴
    for i in range(n):
        if arr[i][1] > k: ## 此时预测为阳
            if arr[i][0] == 1:
                tp += 1
            else:
                fp += 1
        else: ## 此时预测为阴
            if arr[i][0] == 1: 
                fn += 1
            else:
                tn += 1
    tpr = tp / (tp + fn)
    fpr = fp / (tn + fp)
    return [fpr, tpr]


arr.sort(key = lambda x: x[1])

confused_matrix = []
for i in range(n): # 得到横纵坐标
    confused_matrix.append(confuse(arr[i][1]))

res = 0  # 排序，两个维度都单调递增
confused_matrix.sort(key = lambda x:(x[0], x[1]))

if confused_matrix[0] != [0.0, 0.0]:  ## 扩展（0， 0） 和（1， 1）
    confused_matrix.insert(0, [0.0, 0.0])
if confused_matrix[-1] != [1, 1]:
    confused_matrix.append([1.0, 1.0])

## 计算阶梯形面积的函数
def step_area(confused_matrix):
    size = len(confused_matrix)
    area = 0
    tmp = 0
    for i in range(1, size - 1):
        if confused_matrix[i][0] == tmp or confused_matrix[i][1] == confused_matrix[i - 1][1]:
            continue
        little_area = confused_matrix[i - 1][1] * (confused_matrix[i - 1][0] - tmp)
        area += little_area
        tmp = confused_matrix[i - 1][0]
    area += (1 - tmp)
    return area
    
res = step_area(confused_matrix)


print('{:.2f}'.format(res))
## 画出图形
fpr_list, tpr_list = [], []
for fpr, tpr in confused_matrix:
    fpr_list.append(fpr)
    tpr_list.append(tpr)

figure = plt.figure()
plt.title("some pro are the same but their labers are different")
plt.plot(fpr_list, tpr_list)
plt.show()


## 方法2：用计算概率的方法
'''
计算AUC的标准方法
'''
pos = []
neg = []
for i in range(n):
    if arr[i][0] == 1:
        pos.append(arr[i][1])
    else:
        neg.append(arr[i][1])
res = 0
for i in range(len(pos)):
    for j in range(len(neg)):
        if pos[i] > neg[j]:
            res += 1
        elif pos[i] == neg[j]:
            res += 0.5
print('{:.2f}'.format(res / (len(pos) * len(neg))))


