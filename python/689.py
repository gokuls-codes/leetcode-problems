# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description

from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        kSums = [sum([nums[x] for x in range(k)])]
        for i in range(1, n - k + 1):
            kSums.append(kSums[-1] - nums[i - 1] + nums[i + k - 1])

        mem = {}

        def helper(curr, count):
            nonlocal n
            if count == 3 or curr > n - k:
                return 0
            
            if (curr, count) in mem: return mem[(curr, count)]

            inc = kSums[curr] + helper(curr + k, count + 1)
            exc = helper(curr + 1, count)

            mem[(curr, count)] = max(inc, exc)
            return mem[(curr, count)]

        ptr = 0
        res = []

        while ptr <= n - k and len(res) < 3:
            inc = kSums[ptr] + helper(ptr + k, len(res) + 1)
            exc = helper(ptr + 1, len(res))

            if inc >= exc:
                res.append(ptr)
                ptr += k

            else:
                ptr += 1

        return res