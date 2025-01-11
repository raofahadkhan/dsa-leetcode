class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
         # If k is greater than the length of the string, it's impossible to form k palindromes.
        if k > len(s):
            return False
        
        # Count the frequency of each character
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Count the number of characters with odd frequencies
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1
        
        # We can construct k palindromes if k >= odd_count
        return k >= odd_count