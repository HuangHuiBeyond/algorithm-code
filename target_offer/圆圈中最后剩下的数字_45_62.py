from linked_list import SingleLinkedList
class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        ## 用链表来模拟
        loop_list_head, loop_list_tail = self.get_loop_linked_list(n)
        if not loop_list_head:
            return -1
        
        cur_node = loop_list_head
        pre_node = loop_list_tail
        next_node = cur_node.next
        while next_node.next != next_node:
            count = 0
            while count < m - 1:
                pre_node = cur_node
                cur_node = cur_node.next
                count += 1
            next_node = cur_node.next
            pre_node.next = next_node
            cur_node = next_node
            
        return next_node.val
 
    
    def get_loop_linked_list(self, n):
        sll = SingleLinkedList()
        
        head = sll.add_item_from_arr(list(range(n)))
        if head is None:
            return None, None
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = head
        return head, ptr



        ## 直接用list来模拟环形链表,找到删除数字之间的下标变化规律
        def LastRemaining_Solution(self, n, m):
            if n < 1 or m < 1:
                return -1
            arr = list(range(n))
            index = (m - 1) % len(arr)
            while len(arr) > 1:
                
                arr.pop(index)
                index = (index + m - 1) % len(arr)
            return arr[0]


sol = Solution()
res = sol.LastRemaining_Solution(5, 3)
pass

