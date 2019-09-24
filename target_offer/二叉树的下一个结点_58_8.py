'''
调试必备：学习了怎样通过数组来建立满二叉树，学习了怎样得到中序遍历的下一个结点
'''
import math
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def build_tree_from_arr(self, arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        queue = [root]
        front = 0
        index = 1
        while index < len(arr):
            node = queue[front]
            front += 1

            item = arr[index]
            index += 1
            if item != '#':
                node.left = TreeNode(item)
                queue.append(node.left)
            if index >= len(arr):
                break

            item = arr[index]
            index += 1
            if item != '#':
                node.right = TreeNode(item)
                queue.append(node.right)
        return root
    
    def build_parent_tree_from_arr(self, arr):
        if not arr:
            return None
        root = TreeNode(arr[0])
        queue = [root]
        front = 0
        index = 1
        while index < len(arr):
            node = queue[front]
            front += 1

            item = arr[index]
            index += 1
            if item != '#':
                node.left = TreeNode(item)
                queue.append(node.left)
                
                node.left.parent = node
            if index >= len(arr):
                break

            item = arr[index]
            index += 1
            if item != '#':
                node.right = TreeNode(item)
                queue.append(node.right)
                
                node.right.parent = node
        return root

    def get_node_by_value(self, root, value):
        if not root:
            return None
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.val == value:
                return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        next_node = None
        if pNode.right: # 有右子树
            node = pNode.right
            while node.left:
                node = node.left
            next_node = node
        
        elif pNode.parent:
            if pNode.parent.left == pNode:
                next_node = pNode.parent
            else:
                p_cur = pNode
                p_parent = pNode.parent
                while p_parent != None and p_parent.right == p_cur:
                    p_cur = p_parent
                    p_parent = p_parent.parent
                next_node = p_parent
        return next_node


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        next_node = None
        if pNode.right: # 有右子树
            node = pNode.right
            while node.left:
                node = node.left
            next_node = node
        
        elif pNode.next:
            if pNode.next.left == pNode:
                next_node = pNode.next
            else:
                p_cur = pNode
                p_next = pNode.next
                while p_next != None and p_next.right == p_cur:
                    p_cur = p_next
                    p_next = p_next.next
                next_node = p_next
        return next_node

bt = BinaryTree()
s = [1, '#', 2, 3]
arr = [8,6,10,5,7,9,11]
res = bt.build_parent_tree_from_arr(arr)
node = bt.get_node_by_value(res, 7)
final_res = bt.GetNext(node)




pass