# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque() # processing queue to keep track of recorded nodes
        
        queue.append(root) # start with the root initially
        while queue: # keep processing until all nodes in the queue is processed
            length = len(queue)
            level = []
            for i in range(length):
                node = queue.popleft() # grab the front node to be process
                if node: # record to level and collect childrens (for next level)
                    level.append(node.val) # add to the current level list
                    queue.append(node.left) # collect left children
                    queue.append(node.right) # collect right children
            # only record to result non empty level
            if level:
                result.append(level)

        return result
                    

