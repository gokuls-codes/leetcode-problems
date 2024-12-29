# https://leetcode.com/problems/best-sightseeing-pair/

from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        res = 0
        maxFirst = 0
        maxInd = -1

        for i in range(n):
            first = values[i] + i
            second = values[i] - i

            if i > maxInd and res < maxFirst + second:
                res = maxFirst + second

            if maxFirst < first:
                maxFirst = first
                maxInd = i

        return res
        