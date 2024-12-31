# https://leetcode.com/problems/minimum-cost-for-tickets/description/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        mem = {}
        
        def helper(ptr):
            nonlocal n
            if ptr >= n:
                return 0

            if ptr in mem: return mem[ptr]

            r1 = costs[0] + helper(ptr + 1)
            r2 = costs[1] + helper(bisect.bisect_left(days, days[ptr] + 7))
            r3 = costs[2] + helper(bisect.bisect_left(days, days[ptr] + 30))

            mem[ptr] = min(r1, r2, r3)
            return mem[ptr]

        return helper(0)