# 调用的heapq库（首选）
import heapq
A = [5, 6, 4, 2, 8]
def top_k(A, k):
    return heapq.nlargest(k, A)
print(top_k([5, 6, 4, 2, 8], 3))

def findKthLargest(A, k):
    return heapq.nlargest(k, A)[-1]
print(findKthLargest([5, 6, 4, 2, 8], 3))

def heap_sort(A):
    size = len(A)
    heapq.heapify(A)
    return [heapq.heappop(A) for i in range(size)]
print(heap_sort(A))





## 自己写一个堆排序升序排列，是用的大顶堆
A = [5, 6, 4, 2, 8]
def heap_adjust(A,i,size):
    left = 2*i+1
    right = 2*i+2
    max_index = i 
    if left < size and A[left] > A[max_index] :
        max_index = left
    if right < size and A[right] > A[max_index]:
        max_index = right
    if max_index != i:
        temp = A[i]
        A[i] =A[max_index]
        A[max_index] = temp
        heap_adjust(A,max_index,size) #以替换的点为父节点，再调整所在的堆
              
def build_heap(A,size):
    for i in range(size//2,-1,-1):
        heap_adjust(A,i,size)              
        
def heap_sort(A):
    size = len(A)
    build_heap(A,size) #初始化堆
    for i in range(len(A)-1,0,-1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp #将最大元素置于数组后的位置
        heap_adjust(A,0,i)
    return A

def top_k(A, k): # 这种topk算法的效率是很低下的，因为要维护的是长度为size的最大堆，而标准的topk算法只需要维护长度为k的最小堆
    size = len(A)
    build_heap(A, size)
    for i in range(len(A)-1,len(A)-1-k,-1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp #将最大元素置于数组后的位置
        heap_adjust(A,0,i)
    return A[-1:-1-k:-1]

## test
print(heap_sort(A))
print(top_k(A, 2))


# 优化后的topk算法
# topk算法
arr = list(range(10))
def buildMinHeap(arr):
    import math
    for i in range(math.floor(len(arr)/2),-1,-1): ## 只要保证非叶子节点（广义根）节点的值比起子节点要大就行
        heapify(arr,i, len(arr))                  ## 从后往前才能保证堆的性质

def heapify(arr, i, arrLen):
    left = 2*i+1
    right = 2*i+2
    smallest = i
    if left < arrLen and arr[left] < arr[smallest]:
        smallest = left
    if right < arrLen and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        swap(arr, i, smallest)
        heapify(arr, smallest, arrLen)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def topk(arr, k):
    if len(arr) < k:
        raise Exception('数组元素太少')
    arr_heap = arr[:k]
    buildMinHeap(arr_heap)
    for i in range(k, len(arr)):
        if arr[i] > arr_heap[0]:
            arr_heap[0] = arr[i]
            heapify(arr_heap, 0, k)
    # arr_heap.sort(reverse=True)
    # return arr_heap # 输出的是nlargest
    return arr_heap[0] # 输出的是标准topk

arr = [1, 3, 7, 4, 99, 100, 77]
# arr = [1, 3]
print(topk(arr, 3))