from linked_list import SingleLinkedList


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    # 迭代代码
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(None)
        pointer = dummy
        while  pHead1 and  pHead2:
            if pHead1.val < pHead2.val:
                pointer.next = pHead1
                pHead1 = pHead1.next
            else:
                pointer.next = pHead2
                pHead2 = pHead2.next
            pointer = pointer.next
            
        if pHead1:
            pointer.next = pHead1
        if pHead2:
            pointer.next = pHead2
        return dummy.next

    ## 递归代码
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val < pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2






sll = SingleLinkedList()
pHead1 = sll.add_item_from_arr([2, 3, 6])
pHead2 = sll.add_item_from_arr([9999])
sol = Solution()
res = sol.Merge(pHead1, pHead2)
pass





