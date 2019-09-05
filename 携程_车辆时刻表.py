## 题目：给定车辆目的地及出发时刻，同一个目的地的在一组，求最多的组数
## 一定要看清题意，有不懂的多问监考官

S = 'aabbcddeecfgf'
## 重点是每一个字符的最后一个出现的位置
dict = {}
for index, c in enumerate(S):
    dict[c] = index
res , l, r = [], 0, 0
for index, c in enumerate(S):
    if dict[c] > r:
        r = dict[c]
    if index == r:
        res.append(r - l + 1)
        l = index + 1
# return res
for i in range(len(res) - 1):
    print(res[i], end = ",")
print(res[-1])
 
 ## 另一种输出逗号的方法
print(','.join(map(str, res)))  ## 

