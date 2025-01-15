class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of 1 bits in num2
        ones_in_num2 = bin(num2).count('1')
        
        # Initialize result and count of 1s added
        result = 0
        count_ones_added = 0

        # Traverse the bits of num1 from the most significant to the least significant
        for i in range(31, -1, -1):
            if (num1 & (1 << i)) != 0:  # If the ith bit in num1 is set
                if count_ones_added < ones_in_num2:  # Use this bit if we need more 1s
                    result |= (1 << i)
                    count_ones_added += 1

        # If we still need more 1s, set the least significant unset bits
        for i in range(32):
            if count_ones_added == ones_in_num2:
                break
            if (result & (1 << i)) == 0:  # If the ith bit in result is not set
                result |= (1 << i)
                count_ones_added += 1

        return result
