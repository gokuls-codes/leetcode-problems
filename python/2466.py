# https://leetcode.com/problems/count-ways-to-build-good-strings

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
        mem = {}
        MOD = 10**9 + 7

        def helper(currLen):
            if currLen > high: return 0

            if currLen in mem: return mem[currLen]

            res = 0
            if low <= currLen <= high: 
                res += 1

            res += helper(currLen + zero)
            res += helper(currLen + one)

            res %= MOD
            mem[currLen] = res
            return res 

        return helper(0)