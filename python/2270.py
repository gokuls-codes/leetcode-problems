# https://leetcode.com/problems/number-of-ways-to-split-array/

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        req = sum(nums) / 2
        res = 0
        curr = 0

        for i in range(n - 1):
            curr += nums[i]
            if curr >= req: res += 1
            
        return res