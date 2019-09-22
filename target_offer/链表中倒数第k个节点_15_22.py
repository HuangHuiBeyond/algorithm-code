'''
输入一个链表，输出该链表中倒数第k个结点。
'''

'''
这道题的思路很好
如果在只希望一次遍历的情况下, 寻找倒数第k个结点, 可以设置两个指针
第一个指针先往前走k-1步, 然后从第k步开始第二个指针指向头结点
然后两个指针一起遍历
当地一个指针指向尾节点的时候, 第二个指针正好指向倒数第k个结点
推广: 寻找中间节点, 两个指针一起, 第一个指针每次走两步, 第二个指针每次走一步,  快指针指到尾部, 慢指针正好指到中间
'''

# -*- coding:utf-8 -*-

from linked_list import SingleLinkedList
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <= 0:
            return None

        pAHead = head
        pBehind = None

        for i in range(k-1):  ## 在前指针移动的时候就对非正常值进行判断
            if pAHead.next != None:
                pAHead = pAHead.next
            else:
                return None
        pBehind = head
        while pAHead.next != None:
            pAHead = pAHead.next
            pBehind = pBehind.next
        return pBehind
    

    def FindMidNode(self, head):  ## 这双指针的思想非常棒
        if not head:
            return None
        
        pahead = head
        pbehind = head
        while pahead.next:
            pahead = pahead.next.next
            pbehind = pbehind.next
        return pbehind

sll = SingleLinkedList()
sll.add_item_from_arr([1, 2, 3, 4, 5])
sll.add_item_from_arr([1])

sol = Solution()
res = sol.FindMidNode(sll.head)
pass