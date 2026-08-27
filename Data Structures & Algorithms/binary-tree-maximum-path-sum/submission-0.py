# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # helper to find max path sum without split
        def dfs(root):
            if not root:
                return 0 # no additional value gain from None

            # max value from both sides, if they're in the negative, we can not include that path or else it will impact the result
            left_max = max(dfs(root.left), 0)
            right_max = max(dfs(root.right), 0)

            # nax path sum with split
            res[0] = max(res[0], root.val + left_max + right_max)

            return root.val + max(left_max, right_max)
        res = [root.val] # we let the initial known max path sum to only include the root

        dfs(root)
        return res[0]

