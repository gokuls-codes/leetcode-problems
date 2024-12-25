# https://leetcode.com/problems/max-chunks-to-make-sorted/description/

from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        start = 0
        sortedArr = sorted(arr)

        while start < n:
            end = start
            inArr = set()
            inArr.add(arr[end])
            inSortedArr = set()
            inSortedArr.add(sortedArr[end])
            end += 1
            while inArr and inSortedArr and inArr != inSortedArr and end < n:
                # print(inArr, inSortedArr)
                inArr.add(arr[end])
                inSortedArr.add(sortedArr[end])
                end += 1
            ans += 1
            start = end

        return ans
