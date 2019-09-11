## leetcode209
import bisect
n = 5
s = 13
shoubans = [1, 2, 3, 3, 3]
## 滑动窗口法
def minSubArrayLen(s: int, nums: List[int]):
    if not nums : return 0
    left = 0
    cur = 0
    res = float("inf")
    for right in range(len(nums)):
        cur += nums[right]
        while cur >= s:
            res = min(res, right - left + 1)
            cur -= nums[left]
            left += 1
    return res if res != float("inf") else 0

## 二分查找
def minSubArrayLen(s: int, nums: List[int]):  
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s) ## 二分查找这里坑很多
                if nums[i] - nums[loc] >= s:  
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res 