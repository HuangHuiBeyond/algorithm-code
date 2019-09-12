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

def top_k(A, k):
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
print(top_k(A, 1))
