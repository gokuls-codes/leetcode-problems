# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root, 0)])

        while q:
            curr, currLvl = q.popleft()
            if currLvl % 2:
                mem = [(curr, currLvl)]
                while q and q[0][1] % 2:
                    mem.append(q.popleft())
                length = len(mem)
                for i in range(length // 2):
                    mem[i][0].val, mem[-1 - i][0].val  = mem[-1 - i][0].val, mem[i][0].val
                for node, currLvl in mem:
                    if node.left: q.append((node.left, currLvl + 1))
                    if node.right: q.append((node.right, currLvl + 1))
            else:
                if curr.left: q.append((curr.left, currLvl + 1))
                if curr.right: q.append((curr.right, currLvl + 1))


        return root