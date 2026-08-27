# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative solution
        # alternatively we can first convert the tree into a sorted array with in order traversal
        n = 0
        stack = []
        current = root

        while current or stack: # keep going until both the stack is depleted and current points to nothing
            # collect all leftward childs
            while current:
                stack.append(current)
                current = current.left

            # if nothing more to the left, then the top of the stack is our next ordered value
            current = stack.pop()
            n += 1
            if n == k: # target found
                return current.val

            current = current.right # shift to the right, and continue leftwards