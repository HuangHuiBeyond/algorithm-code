## weight:物品重量数组， values：物品价值数组， n：包能装下的最大重量


## 01背包问题：物品装或者不装
'''
有一个容量为 N 的背包，要用这个背包装下物品的价值最大，这些物品有两个属性：体积 w 和价值 v。
定义一个二维数组 dp 存储最大价值，其中 dp[i][j] 表示前 i 件物品体积不超过 j 的情况下能达到的最大价值。设第 i 件物品体积为 w，价值为 v，
根据第 i 件物品是否添加到背包中，可以分两种情况讨论：

1.第 i 件物品没添加到背包，总体积不超过 j 的前 i 件物品的最大价值就是总体积不超过 j 的前 i-1 件物品的最大价值，dp[i][j] = dp[i-1][j]。

2.第 i 件物品添加到背包中，dp[i][j] = dp[i-1][j-w] + v。
第 i 件物品可添加也可以不添加，取决于哪种情况下最大价值更大。因此，0-1 背包的状态转移方程为：
dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

输出是：dp[M][N](其中M为物品个数)

'''
def bag01(weight, values, n):
    if not weight or not n:
        return 0
    m = len(weight)
    dp = [[0] * (n + 1) for i in range(m + 1)]  ## 动态规划的常用技巧，长度加1
    for i in range(1, m + 1): ## i表示物品
        w = weight[i - 1]  ## 用这个技巧的时候，这里要减1
        v = values[i - 1]
        for j in range(1, n + 1):
            if j >= w: ## j表示背包载重
                dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[m][n]
## test
weight = [3, 5, 3, 6]
values = [1, 5, 4, 8]
n = 10
print(bag01(weight, values, n))


## 第416题：分割等和子集
def canPartition(self, nums: List[int]) -> bool:
        ## 背包能不能装下刚好一半的重量
        size = len(nums)
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        dp = [[False] * (target + 1) for _ in range(size)]

        ## 初值条件
        for i in range(target + 1):
            dp[0][i] = False if nums[0] != i else True ## 这里如果单独初始化，考虑大小为size就行了

        for i in range(1, size):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


## 第322题：零钱兑换
def coinChange(self, coins: List[int], amount: int) -> int:
    ## 要学会在一个既定的框架下思考问题，会事半功倍
    ## dp[i] 凑成i元钱时需要的最小硬币数
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] =  min(dp[i], dp[i - coin] + 1)
    return dp[-1] if dp[-1] != float('inf') else -1




## 多维背包问题
## 二个限制对应三维数组
def bag01_multi_dim(weight, volume, values, total_w, total_vol):
    if not weight or not volume or not total_w or not total_vol:
        return 0
    m = len(weight) ## m表示物品个数
    # dp = [[0, 0] * (n + 1) for i in range(m+1)]  ## 动态规划的常用技巧，长度加1
    dp = [[[0]*(total_vol + 1) for _ in range(total_w+1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        w = weight[i - 1]  ## 用这个技巧的时候，这里要减1
        vol = volume[i - 1]
        v = values[i - 1]
        for j in range(1, total_w + 1):
            for k in range(1, total_vol + 1):
                if j >= w and k >= vol:
                    dp[i][j][k] = max(dp[i-1][j-w][k-vol] + v, dp[i-1][j][k])
                else:
                    dp[i][j][k] = dp[i - 1][j][k]
    return dp[m][total_w][total_vol]

## test
total_disk = 15
total_memory = 10
app_list = [[5, 1, 1000], [2,3, 3000], [5, 2,999], [2, 11, 10000]]
w_disk = []
w_memory = []
v = []
for i in range(len(app_list)):
    w_disk.append(app_list[i][0])
    w_memory.append(app_list[i][1])
    v.append(app_list[i][2])
print(bag01_multi_dim(w_disk, w_memory, v, total_disk, total_memory))




