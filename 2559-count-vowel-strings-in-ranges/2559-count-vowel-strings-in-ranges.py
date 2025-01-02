class Solution:
    def isVowelString(self, word: str) -> bool:
        vowels = { 'a', 'e', 'i', 'o', 'u' }
        return word[0] in vowels and word[-1] in vowels
        
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        
        # Create prefix sum array
        prefix_sum: List[int] = [0] * (n + 1)
        
        # Adding the prefix sum to the array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if self.isVowelString(words[i]) else 0)
        
        # Prcoess each query
        results: List[int] = []
        
        for l, r in queries:
            results.append(prefix_sum[r + 1] - prefix_sum[l])
            
        return results
        
        