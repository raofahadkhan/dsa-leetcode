class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)  # Difference array for range updates

        # Apply all shifts using the difference array
        for start, end, direction in shifts:
            increment = 1 if direction == 1 else -1
            diff[start] += increment
            diff[end + 1] -= increment

        # Build the prefix sum to calculate the actual shifts for each index
        shift = [0] * n
        shift[0] = diff[0]
        for i in range(1, n):
            shift[i] = shift[i - 1] + diff[i]

        # Apply the calculated shifts to the string
        result = []
        for i, char in enumerate(s):
            base = ord('a')
            shifted_char_code = ((ord(char) - base + shift[i]) % 26 + 26) % 26 + base
            result.append(chr(shifted_char_code))

        return ''.join(result)

        