class Solution:
    def maxScore(self, s: str) -> int:
        n: int = len(s)
        ones_count: int = 0
        zeroes_count: int = 0
        max_score: int = 0

        for i in range(n):
            if s[i] == '1':
                ones_count += 1
                
        for i in range(n-1):
            if s[i] == '1':
                ones_count -= 1
            else:
                zeroes_count += 1
                
            max_score = max(max_score, ones_count + zeroes_count)
        
        return max_score      