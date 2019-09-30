from linked_list import SingleLinkedList
class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        ## 递归解法
        # if not listNode:
        #     return []
        # return self.printListFromTailToHead(listNode.next) + [listNode.val]

        ## 迭代解法
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        if not stack:
            return []
        res = []
        while stack:
            res.append(stack.pop())
        return res