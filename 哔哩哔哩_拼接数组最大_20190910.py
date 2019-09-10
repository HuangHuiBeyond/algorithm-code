## 拼接数组最大，采用冒泡排序的思想
def maxNumber(nums):
    if not nums:
        return 0
    nums = [str(nums[i]) for i in range(len(nums))]
    size  = len(nums)
    for i in range(size):
        for j in range(i + 1, size):
            if nums[j] + nums[i] > nums[i] + nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return ''.join(nums)

def minNumber(nums):
    if not nums:
        return 0
    nums = [str(nums[i]) for i in range(len(nums))]
    size  = len(nums)
    for i in range(size):
        for j in range(i + 1, size):
            if nums[j] + nums[i] < nums[i] + nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return ''.join(nums)

nums = [31, 310]
nums = [9,3,32,33,303,34]
print(maxNumber(nums))
print(minNumber(nums))