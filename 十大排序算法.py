arr = [9, 7, 8, 2, 3, 0, 4, 6, 5, 1]

## 冒泡排序：
## 思想：每循环一次，挑出最大的放在后面
## 时间复杂度：
## 
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print('bubbleSort: ', bubbleSort(arr))

## 选择排序：
## 思想：选最小的放在第0位，再将第二小的放在第1位
def selectionSort(arr):
    for i in range(len(arr) - 1): ## 前len - 1个数排好，那么最后一个数一定是排好的
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr
print('selectionSort: ', selectionSort(arr))

## 插入排序：
## 思想：每次访问一个数，都使得该数以及之前的数有序
def insertionSort(arr):
    for i in range(len(arr)):
        preIndex = i-1
        current = arr[i]
        while preIndex >= 0 and arr[preIndex] > current:  ## 从后面开始移动保证不被覆盖
            arr[preIndex+1] = arr[preIndex]
            preIndex-=1
        arr[preIndex+1] = current
    return arr
print('insertionSort: ', insertionSort(arr))


## 希尔排序：
def shellSort(arr):
    import math
    gap=1
    while(gap < len(arr)/3):
        gap = gap*3+1  ## 递增序列为1, 4, 13, 40……是常用的递增序列
    while gap > 0:
        for i in range(gap,len(arr)):
            current = arr[i]
            j = i-gap
            while j >=0 and arr[j] > current:
                arr[j+gap]=arr[j]
                j-=gap
            arr[j+gap] = current
        gap = math.floor(gap/3) ## 这样能保证最后一定是1
    return arr
print('shellSort: ' , shellSort(arr))


## 归并排序
def mergeSort(arr):
    import math
    if(len(arr)<2):
        return arr
    middle = math.floor(len(arr)/2)
    left, right = arr[0:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left,right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

print('mergeSort:', mergeSort(arr))


arr = [2, 7, 8, 6, 5]
arr = [8]
arr = [4, 3]
arr = list(range(50, -1, -1))
# 快速排序
def quickSort(arr, left = 0, right = len(arr) - 1):
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):  ## 用的是快慢指针的思想
    pivot = left
    index = pivot+1 ## index是慢指针
    i = index ## i是快指针
    while  i <= right: 
        if arr[i] < arr[pivot]:
            swap(arr, i, index)
            index+=1
        i+=1
    swap(arr,pivot,index-1)
    return index-1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
            
print(quickSort(arr))



# 堆排序
def buildMaxHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1): ## 只要保证非叶子节点（广义根）节点的值比起子节点要大就行
        heapify(arr,i, len(arr))                  ## 从后往前才能保证堆的性质

def heapify(arr, i, arrLen):
    left = 2*i+1
    right = 2*i+2
    largest = i
    if left < arrLen and arr[left] > arr[largest]:
        largest = left
    if right < arrLen and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        swap(arr, i, largest)
        heapify(arr, largest, arrLen)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapSort(arr):
    buildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        swap(arr,0,i)  
        heapify(arr, 0, i) ## 这步维护最大堆的性质，并且长度减小了（已经完成排序的不再参与最大堆的建设）
    return arr

print(heapSort(arr))


## 计数排序 需要额外开辟空间，也需要知道最大值是多少，是用空间换时间的一种体现
## 有时候空间复杂度过大难以接受， 并且不能排序小数
def countingSort(arr, maxValue):
    bucketLen = maxValue+1
    bucket = [0]*bucketLen
    sortedIndex =0
    arrLen = len(arr)
    for i in range(arrLen):
        # if not bucket[arr[i]]:
        #     bucket[arr[i]]=0
        bucket[arr[i]]+=1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex+=1
            bucket[j]-=1
    return arr
print(countingSort(arr, 9))

## 桶排序


## 基数排序





