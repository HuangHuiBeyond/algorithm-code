## 用状态机来完成6道题目

## 只能买卖一次
def max_profit_1(prices):
    ## 状态要学会变通，如果只能一次的话，所有变量都要在最多只能一次的前提下更新状态
    if not prices:
        return 0
    size = len(prices)
    dp = [[0, 0] for _ in range(size)] ## 是否留有股票（0：不留有，1：留有）
    dp[0][1] = -prices[0]              ## 在buy的时候把交易次数减小1
    for i in range(1, size):
        
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1],  0 - prices[i])
    return dp[size - 1][0]


    ## 把空间复杂度降为1
    if not prices:
        return 0
    size = len(prices)
    dp_i_0 = 0 ## 是否留有股票（0：不留有，1：留有）
    dp_i_1 = -prices[0]              ## 在buy的时候把交易次数减小1
    for i in range(1, size):
        
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1,  0 - prices[i])
    return dp_i_0


## 可以买卖无限次
def max_profit_infinite(prices):
    if not prices:
            return 0
    size = len(prices)
    dp_i_0 = 0
    dp_i_1 = -prices[0]
    for i in range(1, size):
        temp = dp_i_0  ## 为了节省空间复杂度，这里保存中间状态
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0


## 只能买2次，标准状态机
def max_profit_2(prices):
    if not prices:
        return 0
    size = len(prices)
    k = 2
    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(size)]
    for i in range(0, size):
        for j in range(1, k + 1):
            if i == 0:
                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i] ## 这里的初始化逻辑很关键
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j -1][0] - prices[i])
    return dp[size - 1][k][0]


## 只能买卖k次
def max_profit_k(k, prices):
    
    ## 处理k过大导致超时的问题，用贪心解决
    def greedy(prices):
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i] - prices[i-1]
        return res


    if not prices:
        return 0
    size = len(prices)
    if k > size // 2:
        return greedy(prices)

    dp = [[[0, 0] for _ in range(k + 1)] for _ in range(size)]
    for i in range(0, size):
        for j in range(1, k + 1):
            if i == 0:
                dp[i][j][0] = 0
                dp[i][j][1] = -prices[i] ## 这里的初始化逻辑很关键
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j -1][0] - prices[i])
    return dp[size - 1][k][0]


## 无限次交易有冷冻期
def max_profit_infinite_cooldown(prices):
    if not prices:
        return 0
    size = len(prices)
    dp_i_0 = 0
    dp_i_1 = -prices[0]
    dp_pre_0 = 0
    for i in range(1, size):
        temp = dp_i_0  ## 为了节省空间复杂度，这里保存中间状态
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
        dp_pre_0 = temp  ## 保存的是前前一天的状态
    return dp_i_0


## 无限次有手续费
def max_profit_infinite_fee(prices, fee):
    if not prices:
        return 0
    size = len(prices)
    dp_i_0 = 0
    dp_i_1 = -prices[0] - fee
    for i in range(1, size):
        temp = dp_i_0  ## 为了节省空间复杂度，这里保存中间状态
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i] - fee)         
    return dp_i_0

