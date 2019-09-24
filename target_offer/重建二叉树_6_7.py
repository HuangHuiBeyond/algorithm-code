class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root_val = pre[0]
        left, right = [], []
        for i in range(len(tin)):
            if tin[i] == root_val:
                left = tin[:i]
                right = tin[i + 1:]
                break
        pre_left, pre_right = [], []
        for j in pre:
            if j in left:
                pre_left.append(j)
            elif j in right:
                pre_right.append(j)
        
                
        root = TreeNode(root_val)
        root.left = self.reConstructBinaryTree(pre_left, left)
        root.right = self.reConstructBinaryTree(pre_right, right)
        return root
pre, tin = [1,2,3,4,5,6,7], [3,2,4,1,6,5,7]
sol = Solution()
root = sol.reConstructBinaryTree(pre, tin)
pass