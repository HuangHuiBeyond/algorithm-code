import bisect
from typing import List
## 第718题：最长重复子数组（要求连续）
### 动态规划：重点是dp定义：dp[i][j]表示B[:j + 1]以j为结束到A[:i + 1]以i为结束的最长公共子数组
### 关键是以……为结束，这样的话最后还要遍历一遍取最大值
def findLength(self, A, B) -> int:
    if not A or not B:
            return 0
    size_a, size_b = len(A), len(B)
    dp = [[0] * (size_b + 1) for _ in range(size_a + 1)] ## 利用到了python特殊的-1为最后一个数的特性来做初始化
    for i in range(1, size_a + 1):
        for j in range(1, size_b + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
    # return max([max(dp[i]) for i in range(size_a + 1)])  ## 二维数组里面取最大值
    return max(max(row) for row in dp)

## 变体：要求输出该字符串
def printLongestSubString(A, B):
    if not A or not B:
            return []
    size_a, size_b = len(A), len(B)
    dp = [[0] * (size_b + 1) for _ in range(size_a + 1)] ## 利用到了python特殊的-1为最后一个数的特性来做初始化
    for i in range(1, size_a + 1):
        for j in range(1, size_b + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
    # return max([max(dp[i]) for i in range(size_a + 1)])  ## 二维数组里面取最大值
    res = 0
    temp_i = 0
    for i in range(size_a + 1):
        for j in range(size_b + 1):
            if dp[i][j] > res:
                temp_i = i - 1
                
                res = dp[i][j]
    if res:
        return A[temp_i - res + 1:temp_i + 1]
    else:
        return []
## test 最长重复子数组
print(printLongestSubString([1,2,3,2,1,4], [3,2,1,4,7]))
print(printLongestSubString([], [7]))
print(printLongestSubString([1], [3]))    
print(printLongestSubString([1, 2], [3, 2]))
print(printLongestSubString([1, 2, 3], [3, 2, 1, 2, 3, 4, 5]))
print(printLongestSubString([], []))






## lintcode第77题：最长公共子序列
def longestCommonSubsequence(A, B):
    # write your code here
    if not A or not B:
        return 0
    size_a, size_b = len(A), len(B)
    # dp = [[0] * (size_b + 1) for _ in range(size_a + 1)] ## 利用到了python特殊的-1为最后一个数的特性来做初始化
    for i in range(1, size_a + 1):
        for j in range(1, size_b + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[size_a][size_b]

# 变体：要求输出该字符串
## 当A, B是字符串的时候
def printLongestCommonSubsequence(A, B):

    size_a = len(A)
    size_b = len(B)
    dp = [[0] * (size_b + 1) for _ in range(size_a + 1)] ## 利用到了python特殊的-1为最后一个数的特性来做初始化
    set_of_Lcs = set()
    def longestCommonSubsequence(A, B):
        # write your code here
        if not A or not B:
            return 0
        for i in range(1, size_a + 1):
            for j in range(1, size_b + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[size_a][size_b]

    def traceback(i, j, s):
        while i > 0 and j > 0:
            if A[i - 1] == B[j - 1]:
                s += A[i - 1]
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                elif dp[i - 1][j] < dp[i][j - 1]:
                    j -= 1
                else:
                    traceback(i - 1, j, s)
                    traceback(i, j - 1, s)
                    return
        set_of_Lcs.add(s[::-1])

    longestCommonSubsequence(A, B)
    traceback(size_a, size_b, '')
    return set_of_Lcs

## test
A = 'ABCBDAB'
B = 'BDCABA'
print(printLongestCommonSubsequence(A, B))

## 当A，B是整数数组的时候
def printLongestCommonSubsequence(A, B):

    size_a = len(A)
    size_b = len(B)
    dp = [[0] * (size_b + 1) for _ in range(size_a + 1)] ## 利用到了python特殊的-1为最后一个数的特性来做初始化
    set_of_Lcs = set()
    def longestCommonSubsequence(A, B):
        # write your code here
        if not A or not B:
            return 0
        for i in range(1, size_a + 1):
            for j in range(1, size_b + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[size_a][size_b]

    def traceback(i, j, s):
        while i > 0 and j > 0:
            if A[i - 1] == B[j - 1]:
                s += str(A[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                elif dp[i - 1][j] < dp[i][j - 1]:
                    j -= 1
                else:
                    traceback(i - 1, j, s)
                    traceback(i, j - 1, s)
                    return
        set_of_Lcs.add(s[::-1])

    longestCommonSubsequence(A, B)
    traceback(size_a, size_b, '')
    return set_of_Lcs

## test
print(printLongestCommonSubsequence([1,2,3,2,1,4, 5, 3, 4, 6, 7], [3,2,1,4,7, 8, 5, 8, 7, 6]))
print(printLongestCommonSubsequence([], [7]))
print(printLongestCommonSubsequence([1], [3]))    
print(printLongestCommonSubsequence([1, 6], [3, 1]))
print(printLongestCommonSubsequence([3, 2, 3, 6, 4, 5], [8, 7, 1, 2, 3, 4, 5]))
print(printLongestCommonSubsequence([], []))
    



## 第300题：最长严格上升序列
def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        if not nums:
            return 0
        size = len(nums)
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # 贪心算法 + 二分查找右边界(逻辑有误，因为如果有重复数字，要求严格上升是过不了的)
        if not nums:
            return 0
        q = [nums[0]]
        for i in nums[1:]:
            if i > q[-1]:
                q += [i]
            else:
                l = 0
                r = len(q) - 1
                while l < r:
                    mid = (l + r + 1) >> 1
                    if q[mid] > i:
                        r = mid - 1
                    else:
                        l = mid
                if l == 0 and q[l] > i or q[l] == i: ## 最关键的是逻辑要清晰，知道问题的不同在哪里
                    q[l] = i
                else:
                    q[l + 1] = i
        return len(q)

        # 贪心算法 + 查找左边界 + 手写二分查找
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        q = [nums[0]] ## 这里不够鲁棒
        for i in nums[1:]:
            if i > q[-1]:
                q += [i]
            else:
                l = 0
                r = len(q) - 1
                while l < r:
                    mid = (l + r ) >> 1
                    if q[mid] < i:
                        l = mid + 1
                    else:
                        r = mid
                
                q[l] = i
        return len(q)

        ## 贪心算法 + 调库实现二分查找
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        q = [nums[0]] 
        for i in nums[1:]:
            if i > q[-1]:
                q += [i]
            else:
                q[bisect.bisect_left(q, i)] = i
        return len(q)

# 最长非严格上升序列
def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        if not nums:
            return 0
        size = len(nums)
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[j] <= nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

        # 贪心算法 + 二分查找右边界(逻辑有误，因为如果有重复数字，要求严格上升是过不了的)
        if not nums:
            return 0
        q = [nums[0]]
        for i in nums[1:]:
            if i >= q[-1]:
                q += [i]
            else:
                l = 0
                r = len(q) - 1
                while l < r:
                    mid = (l + r + 1) >> 1
                    if q[mid] > i:
                        r = mid - 1
                    else:
                        l = mid
                if l == 0 and q[l] > i or q[l] == i: ## 最关键的是逻辑要清晰，知道问题的不同在哪里
                    q[l] = i
                else:
                    q[l + 1] = i
        return len(q)

        # 贪心算法 + 查找右边界 + 手写二分查找
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        q = [nums[0]] 
        for i in nums[1:]:
            if i >= q[-1]:
                q += [i]
            else:
                l = 0
                r = len(q) - 1
                while l < r:  
                    mid = (l + r + 1) >> 1
                    if q[mid] > i:
                        r = mid - 1
                    else:
                        l = mid
                if q[l] > i:
                    q[l] = i
                else:
                    q[l + 1] = i
        return len(q)

        ## 贪心算法 + 调库实现二分查找
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        q = [nums[0]] 
        for i in nums[1:]:
            if i >= q[-1]: ## 这里也是区别
                q += [i]
            else:
                q[bisect.bisect_right(q, i)] = i ## 与严格上升的区别在这里
        return len(q)

## 第354题：俄罗斯套娃信封问题：多维严格上升子序列
def maxEnvelopes(envelopes: List[List[int]]) -> int:
        # 贪心算法加二分查找, 严格升序对应查找最左边界，替换左边界即可
        if not envelopes:
            return 0
        size = len(envelopes)
        envelopes.sort(key = lambda x:(x[1], -x[0])) ## 先按照x[1]升序，遇到相同的再按照x[0]降序排列
        nums = envelopes.copy()
        q = [nums[0][0]]
        if size == 1:
            return len(q)
        for i in range(1, size):
            if nums[i][0] > q[-1]:
                q.append(nums[i][0])
            else:
                index = bisect.bisect_left(q, nums[i][0])
                q[index] = nums[i][0]
        return len(q)


# 牛客2019真题之搭积木：多维非严格上升子序列
def building_blocks(blocks):
    # 贪心算法加二分查找, 严格升序对应查找最左边界，替换左边界即可
        if not blocks:
            return 0
        size = len(blocks)
        blocks.sort(key = lambda x:x[1]) ## 先按照x[1]升序即可
        nums = blocks.copy()
        q = [nums[0][0]]
        if size == 1:
            return len(q)
        for i in range(1, size):
            if nums[i][0] >= q[-1]:
                q.append(nums[i][0])
            else:
                index = bisect.bisect_right(q, nums[i][0])
                q[index] = nums[i][0]
        return len(q)
## test
print(building_blocks([[2, 2], [2, 4], [3, 3], [2, 5], [4, 5]]))

## 第14题：最长公共前缀
def longestCommonPrefix(self, strs) :
    ## 水平扫描或者分治策略都可以
        ## 简化的水平扫描
        # if len(strs) == 0:
        #     return ''
        # if "" in strs:
        #     return ""
        # for i in range(len(strs[0])):
        #     char = strs[0][i]
        #     for _str in strs:
        #         if i == len(_str) or char != _str[i]: ## 用i来寻找最小长度的方法清新独特，且
        #             return strs[0][:i]                ## 其必须首先判断
        # return strs[0]  ## 注意情况的完备性，这句return很重要

        ## 分治策略
        if len(strs) == 0 or "" in strs:
            return ''
        else:
            return self.lcp(strs, 0, len(strs)-1) 
        
    def common_prefix(self, str1, str2): ## 关键步骤：分治之后的合并
        for i in range(len(str1)):
            if i == len(str2) or str1[i] != str2[i]:
                return str1[:i]
        return str1

    def lcp(self, strs, l, r):
        if l == r: ## 停止递归
            return strs[l]
        mid = (l + r) // 2  ## 如何分:取二分的官方解法
        left_lcp = self.lcp(strs, l, mid) ## 注意两个集合是补集
        right_lcp = self.lcp(strs, mid+1, r)

        return self.common_prefix(left_lcp, right_lcp) 


# 第53题：最大子序和
## 动态规划：dp[i]以i下标为结束的最大和
def maxSubArray(self, nums: List[int]) -> int:
        ## 类动态规划，但是没有dp数组，不够经典
        ## 对空间复杂度进行优化
        # sub_sum = 0
        # res = nums[0]
        # for num in nums:
        #     if sub_sum < 0:
        #         sub_sum = num
        #     else:
        #         sub_sum += num
        #     res = max(res, sub_sum)
        # return res

        ## dp动态规划
        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = dp[i] if dp[i] > res else  res
        return res


## 第152题：乘积最大子序列和
def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

