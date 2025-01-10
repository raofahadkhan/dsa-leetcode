from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # Combine all requirements from words2 into a single frequency Counter
        max_count: Counter = Counter()
        for word in words2:
            for char, count in Counter(word).items():
                max_count[char] = max(max_count[char], count)
        
        # Check each word in words1
        result: List[str] = []
        for word in words1:
            word_count: Counter = Counter(word)
            if all(word_count[char] >= max_count[char] for char in max_count):
                result.append(word)
        
        return result