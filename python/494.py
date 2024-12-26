# https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = {}
        
        def helper(curr, index):
            nonlocal n, target
            if index == n:
                if curr == target:
                    return 1
                return 0

            if (curr, index) in mem: return mem[(curr, index)]

            v1 = helper(curr + nums[index], index + 1)
            v2 = helper(curr - nums[index], index+ 1)

            mem[(curr, index)] = v1 + v2
            return v1 + v2

        return helper(0, 0)
        