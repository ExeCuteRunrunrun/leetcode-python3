# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.
# The tree additionally satisfies the binary search property, which states that the key in each node must be greater than or 
# equal to any key stored in the left sub-tree, and less than or equal to any key stored in the right sub-tree
# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
#      10
#     / \
#    5   15
#  / |   |  \
# 3  7  none 18
# Output: 32

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

################ 1. iteration ############################################
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        summ = 0
        
        # stack is a list containing firstly the root, then we will add possible nodes to stack
        stack = [root]
        # print(stack) -------- $[<precompiled.treenode.TreeNode object at 0x7f2d7dcb9a90>]
        
        while stack:
            node = stack.pop()
            
            if node:
                # print(node)     --------- $<precompiled.treenode.TreeNode object at 0x7f2d7dcb9a90>
                # print(node.val) --------- $10
                # print(stack)    --------- $[]
                if L <= node.val <= R:
                    summ += node.val
                if L < node.val: # node.val == 5, L==7: no need to check the left child
                    stack.append(node.left)
                if R > node.val: # node.val == 5, R==15: still check the right child
                    stack.append(node.right)
        return summ
        
       
################ 2. recursive #############################################

    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                self.ans += node.val*(L <= node.val <= R)
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans
        
        
################ 3. recursive one line #######################################

    def rangeSumBST(self, root, L, R):
    # and ------- return the biggest value and ensures non-none value
    # or -------- return the first non-none value
        return root and root.val * (L<= root.val <=R) + rangeSumBST(self, root.left, L, R) + rangeSumBST(self, root.right, L, R) or 0
