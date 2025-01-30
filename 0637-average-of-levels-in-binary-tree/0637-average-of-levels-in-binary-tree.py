from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = deque([root])
        res = []

        while q:
            level_sum = 0
            level_size = len(q)
            for _ in range(len(q)):
                curr = q.popleft()
                level_sum += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            average = level_sum / level_size
            res.append(average)
        return res