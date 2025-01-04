class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            l, r = s.find(c), s.rfind(c)
            if l != -1 and r != -1 and r - l > 1:
                ans += len(set(s[l + 1:r]))
        return ans
        