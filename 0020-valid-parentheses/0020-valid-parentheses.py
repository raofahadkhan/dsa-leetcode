class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_paren = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif stack and close_paren[ch] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False
