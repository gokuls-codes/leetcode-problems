# https://leetcode.com/problems/count-vowel-strings-in-ranges/description/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        n = len(words)
        mem = [0] * n
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                mem[i] += 1

        prefixSum = [0]
        for i in range(n):
            prefixSum.append(prefixSum[-1] + mem[i])

        return [prefixSum[e + 1] - prefixSum[s] for s,e in queries]