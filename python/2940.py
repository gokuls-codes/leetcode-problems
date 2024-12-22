from typing import List
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        maxIndex = []
        q = len(queries)
        n = len(heights)
        res = [-1 for _ in range(q)]
        mem = [[] for _ in range(n)]

        for i in range(q):
            a, b = queries[i]
            if a < b and heights[a] < heights[b]: res[i] = b
            elif a > b and heights[a] > heights[b]: res[i] = a
            elif a == b: res[i] = a
            else: mem[max(a, b)].append((max(heights[a], heights[b]), i))

        for i in range(n):
            while maxIndex and maxIndex[0][0] < heights[i]:
                _, qIndex = heapq.heappop(maxIndex)
                res[qIndex] = i
            
            for query in mem[i]:
                heapq.heappush(maxIndex, query)

        return res