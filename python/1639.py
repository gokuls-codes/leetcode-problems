# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary

from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words[0])
        m = len(target)

        MOD = 10**9 + 7

        mem = [0] * (m + 1)
        mem[0] = 1

        count = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for word in words:
                count[i][ord(word[i]) - ord('a')] += 1

        for i in range(n):
            for j in range(m - 1, -1 , -1):
                mem[j + 1] += mem[j] * count[i][ord(target[j]) - ord('a')]
                mem[j + 1] %= MOD

        return mem[m]