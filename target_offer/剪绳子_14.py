# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        
        ## 动态规划算法
        # if number == 2:
        #     return 1
        # if number == 3:
        #     return 2
        # dp = [0] * (number + 1) ## 长度为number可以剪出来的最大乘积， 注意一定得剪
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 3
        # for i in range(4, number + 1):
        #     for j in range(1, i // 2 + 1): ## 可以进行优化
        #         dp[i] = max(dp[i], dp[j] * dp[i - j])
        # return dp[number]

        ## 贪心算法
        
        if number == 2:
            return 1
        if number == 3:
            return 2
        timesOf3 = number // 3
        if number - 3 * timesOf3 == 1:
            timesOf3 -= 1
        timesOf2 = (number - 3 * timesOf3) // 2
        return pow(3, timesOf3) * pow(2, timesOf2)
        

sol = Solution()
res = sol.cutRope(8)
print(res)


