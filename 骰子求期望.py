def expection(a):
    ## 数组a中的每一个数代表色子的点数a[i](取值范围为1-a[i])，一次试验是把每一个色子掷一次，试验结果是取值最大的数，求试验结果期望
    ## 思路:用迭代的思路求解，取值小于等于i的概率 - 取值小于等于(i - 1)的概率 = 取值一定含i的概率
    if not a:
        return 0
    size = len(a)
    expec = 0 
    ans = []  # 存储每一个可能结果的概率
    maxi = max(a)
    s = 1
    tmp = 0
    for i in range(1, maxi + 1):
        tmp = s
        s = 1
        if i == 1:
            tmp = 0
        for j in range(size):
            if a[j] < i:
                continue
            s *= (i / a[j])
        ans.append((i, (s - tmp)))
        expec += i * (s - tmp)
    return (expec, ans)

res, ans = expection([2, 3, 3])
print(res, ans)



# 易于理解版版本
a = [2, 2]
a.sort()
def expecation(a):
    a.sort()
    maxi = max(a)
    A = 1
    for i in range(len(a)):
        A *= a[i]
    p = []
    for i in range(1, maxi + 1):
        pi = 1/A
        if i == 1:
            p.append(pi)
        else:
            for j in range(len(a)):
                if i < a[j]:
                    pi *= i
                else:
                    pi *= a[j]
            p.append(pi - sum(p[:]))
    res = 0
    for i in range(1, maxi + 1):
        res += i * p[i - 1]
    return res
print(expecation(a))