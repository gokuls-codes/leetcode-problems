# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        mem = []
        q = deque([(root, 0)])

        while q:
            curr, currLvl = q.popleft()
            if currLvl < len(mem): mem[currLvl] = max(mem[currLvl], curr.val)
            else: mem.append(curr.val)

            if curr.left: q.append((curr.left, currLvl + 1))
            if curr.right: q.append((curr.right, currLvl + 1))

        # maxLvl = max(mem.keys())

        # return [mem[x] for x in range(maxLvl + 1)]
        return mem
