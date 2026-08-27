# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True

            if p and q and p.val == q.val: # same node -> recursive
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            
            # else, not the same
            return False

        # assumption: a None subtree is always a subtree of another tree
        if not subRoot:
            return True
        # An empty tree cannot contain any subtree
        if not root:
            return False

        # Check if the current level tree has the subtree
        if sameTree(root, subRoot):
            return True

        # Else, check lower level if it has the subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)