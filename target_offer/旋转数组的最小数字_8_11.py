class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        l = 0
        r = len(rotateArray) - 1
        while r - l != 1:
            mid = (l + r) >> 1
            if rotateArray[mid] == rotateArray[l] and rotateArray[mid] == rotateArray[r]:
                return self.linear_search(rotateArray, l, r)

            if rotateArray[mid] >= rotateArray[l]:
                l = mid
            else:
                r = mid
        return rotateArray[r]
    
    def linear_search(self, rotateArray, l, r):
        res = rotateArray[l]
        for i in range(l + 1, r + 1):
            if rotateArray[i] < res:
                res = rotateArray[i]
        return res
    
sol = Solution()
# arr = [3, 4, 5, 1, 2]
arr = [1, 0, 1, 1, 1]
res = sol.minNumberInRotateArray(arr)
print(res)