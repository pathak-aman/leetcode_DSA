# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def height_bal(root):
            if not root:
                return 0, True
            lh, l_bal = height_bal(root.left)
            rh, r_bal = height_bal(root.right)

            if l_bal and r_bal and abs(lh-rh) <= 1:
                return 1 + max(lh,rh), True
            else:
                return 1 + max(lh,rh), False
        
        return height_bal(root)[1]
        