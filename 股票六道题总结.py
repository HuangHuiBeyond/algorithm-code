## 用状态机来完成6道题目

### 初始化一个三维度数组
## 用状态机来完成
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