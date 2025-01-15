class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # If the length of s is odd, it cannot be valid
        if len(s) % 2 != 0:
            return False

        # Left-to-right pass to ensure balance of '('
        open_count = 0  # Count of effective '('
        flexible_count = 0  # Count of flexible positions
        
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    open_count += 1
                else:
                    open_count -= 1
            else:
                flexible_count += 1

            # If open_count goes negative, use flexibility to balance
            if open_count < 0:
                if flexible_count > 0:
                    flexible_count -= 1
                    open_count += 1
                else:
                    return False  # Unrecoverable imbalance
        
        # Right-to-left pass to ensure balance of ')'
        close_count = 0  # Count of effective ')'
        flexible_count = 0  # Reset flexible count
        
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    close_count += 1
                else:
                    close_count -= 1
            else:
                flexible_count += 1

            # If close_count goes negative, use flexibility to balance
            if close_count < 0:
                if flexible_count > 0:
                    flexible_count -= 1
                    close_count += 1
                else:
                    return False  # Unrecoverable imbalance
        
        return True