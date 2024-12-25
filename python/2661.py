# https://leetcode.com/problems/first-completely-painted-row-or-column/description/

from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        matrixMem = {}

        for i in range(m):
            for j in range(n):
                matrixMem[mat[i][j]] = (i, j)

        rowsMem = [0] * m
        colsMem = [0] * n

        for i in range(m*n):
            num = arr[i]
            r, c = matrixMem[num]
            colsMem[c] += 1
            rowsMem[r] += 1

            if colsMem[c] == m or rowsMem[r] == n:
                return i