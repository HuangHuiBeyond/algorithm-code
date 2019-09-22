## 给定一个数组(如1到20这20个数)摆成一个环，要求相邻的两个数的和是一个素数。

## 判断一个数是否是一个素数
import math
def is_prime_number(n):
    for i in range(2, math.floor((math.sqrt(n)) + 1)):
        if n % i == 0:
            return False
    return True

## test
print(is_prime_number(7))

## 输出100以内的素数, 1， 0不是质数也不是合数
def get_prime_number(start, end):
    res = []
    for i in range(start, end + 1):
        if is_prime_number(i):
            res.append(i)
    return res
print(len(get_prime_number(2, 100)))

## 输出1到6的全排列


def permute(arr):
    res = []
    size = len(arr)
    def backtrack(arr, temp):
        if len(temp) > 1:
            for i in range(len(temp) - 1):
                if not is_prime_number(temp[i] + temp[i + 1]):  ## 这里进行剪枝
                    return
        if len(temp) == size:
            if not is_prime_number(temp[0] + temp[-1]):  ## 这里进行判断是否符合条件
                return 
        if not arr:
            res.append(temp)
            return
        for i in range(len(arr)):
            backtrack(arr[:i] + arr[i + 1:], temp + [arr[i]])
    backtrack(arr, [])
    return res
arr = [i for i in range(1, 20)]
arr = [3, 7, 5, 4, 6]
res = permute(arr)
print(res)
print(len(res))


## 推广：数字排列成环，每一个数都小于前一个数和后一个数的和
def number_loop(arr):
    arr.sort()
    res = []
    size = len(arr)
    
    def backtrack(arr, temp):
        if len(temp) > 2:
            for i in range(1, len(temp) - 1):
                if temp[i] > temp[i - 1] + temp[i + 1]:
                    return  
        if len(temp) == size:
            if  temp[0] > temp[-1] + temp[1] or \
                 temp[-1] > temp[-2] + temp[0]:
                    return

        if not arr:
            res.append(temp)
        for i in range(len(arr)):
            if i - 1 >= 0 and arr[i] == arr[i - 1]:
                continue
            backtrack(arr[:i] + arr[i + 1:], temp + [arr[i]])
    backtrack(arr, [])
    return res
arr = [3, 7, 5, 4, 6]
arr = [3, 3, 4]
arr = [7, 100, 105, 6]
res = number_loop(arr)
print(res)
print(len(res))

## 定义可由数组平移得到的归为同一个环
ans = int(len(res) / len(arr) / 2)
print(ans)

        
        
