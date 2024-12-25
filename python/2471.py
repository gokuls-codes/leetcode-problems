# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minSwaps(self, arr: List[int]) -> int:
        n = len(arr)
        arrpos = [*enumerate(arr)]
        arrpos.sort(key=lambda it: it[1])

        vis = {k: False for k in range(n)}

        ans = 0
        for i in range(n):

            if vis[i] or arrpos[i][0] == i:
                continue

            cycle_size = 0
            j = i

            while not vis[j]:
                vis[j] = True
                j = arrpos[j][0]
                cycle_size += 1

            if cycle_size > 0:
                ans += (cycle_size - 1)

        return ans

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        mem = defaultdict(list)
        q = deque([(root, 0)])
        res = 0

        while q:
            currLvl = q[0][1]
            currLvlNodes = []
            while q and q[0][1] == currLvl:
                curr, _ = q.popleft()
                currLvlNodes.append(curr.val)
                if curr.left: q.append((curr.left, currLvl + 1))
                if curr.right: q.append((curr.right, currLvl + 1))
            if currLvlNodes:
                res += self.minSwaps(currLvlNodes)

        return res