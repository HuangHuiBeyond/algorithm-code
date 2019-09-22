from linked_list import SingleLinkedList

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    # 迭代解法
    def ReverseList(self, pHead):
        # write code here
        p_reverse_head = ListNode(None)
        cur_node = pHead
        pre_node = None
        while cur_node is not None:
            next_node = cur_node.next  ## 需要提前保存好下一个节点的值
            if next_node is None:
                p_reverse_head = cur_node
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        return p_reverse_head
    
    ## 递归解法
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead  ## 把None换掉
            pHead.next = None  ## 最后要接一个None
            return pReversedHead




sll = SingleLinkedList()
sll.add_item_from_arr([1, 2])
sol = Solution()
res = sol.ReverseList(sll.head)
pass