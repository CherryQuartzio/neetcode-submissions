# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node: # empty node is valid by itself
                return True

            if not (node.val < right and node.val > left):
                # not within correct bound, which violates BST rule
                return False

            # current level is fine, keep checking at lower level
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        # initial check at root
        return valid(root, float("-inf"), float("inf")) 