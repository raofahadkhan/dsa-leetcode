class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)  # Keep track of frequency of each number
        result = []
        count = 0
        
        # Process both arrays simultaneously
        for i in range(n):
            # Process number from array A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                count += 1
                
            # Process number from array B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                count += 1
                
            result.append(count)
        
        return result