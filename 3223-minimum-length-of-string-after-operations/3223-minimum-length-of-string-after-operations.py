class Solution:
    def minimumLength(self, s: str) -> int:
        # Create a dictionary to store character frequencies
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Calculate the minimum length based on character frequencies
        min_length = 0
        for count in freq.values():
            min_length += 1 if count % 2 != 0 else 2
        
        return min_length
