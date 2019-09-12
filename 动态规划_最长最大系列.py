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
    
    
