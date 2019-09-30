from linked_list import SingleLinkedList
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        ## 暴力法
        # write code here
        if not pHead1 or not pHead2:
            return None
        while pHead1:
            if self.search(pHead2, pHead1.val):
                return pHead1
            pHead1 = pHead1.next
        return None
            
        
    
    def search(self, head, item_value):
        if not head:
            return False
        while head:
            if head.val == item_value:
                return True
            head = head.next
        return False

        ## 解题妙法
        if not pHead1 or not pHead2:
            return None
        size1 = self.get_size(pHead1)
        size2 = self.get_size(pHead2)
        flag = False
        if size1 > size2:
            k = size1 - size2
            flag = True
        else:
            k = size2 - size1
        if flag:
            for i in range(k):
                pHead1 = pHead1.next
        else:
            for i in range(k):
                pHead2 = pHead2.next
        while pHead1:
            if pHead1.val == pHead2.val:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return None

    def get_size(self, head):
        if not head:
            return 0
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    ## 解法三：调用辅助栈(利用栈后入先出的特性)
        if not pHead1 or not pHead2:
            return None
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        res_temp1 = None
        while stack1 and stack2:
            temp1 = stack1.pop()
            temp2 = stack2.pop()
            
            if temp1.val != temp2.val:
                return res_temp1
            res_temp1 = temp1
            

        return res_temp1



         


 

sll = SingleLinkedList()
pHead1 = sll.add_item_from_arr([1, 2, 3, 4, 5])
pHead2 = sll.add_item_from_arr([1, 2, 3, 4, 5])
sol = Solution()
res = sol.FindFirstCommonNode(pHead1, pHead2)
pass
