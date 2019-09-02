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