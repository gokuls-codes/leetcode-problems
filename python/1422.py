# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

class Solution:
    def maxScore(self, s: str) -> int:
        left_score = 1 if s[0] == '0' else 0
        right_score = s.count('1')
        
        if s[0] == '1':
            right_score -= 1
        
        max_score = left_score + right_score
        
        for i in range(1, len(s)-1):
            if s[i] == '1':
                right_score -= 1
            else:
                left_score += 1
            
            max_score = max(max_score, right_score + left_score)
            
            
        return max_score