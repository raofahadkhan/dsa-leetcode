class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')':'(', '}':'{', ']':'['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif stack and bracket_map[ch] == stack[-1]:
                stack.pop()
            else:
                return False

        return True if not stack else False
