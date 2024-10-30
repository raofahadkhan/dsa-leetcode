class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_paren = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in close_paren.values():  # if ch is an opening bracket
                stack.append(ch)
            elif ch in close_paren:  # if ch is a closing bracket
                top_element = stack.pop() if stack else '#'
                if close_paren[ch] != top_element:
                    return False
            else:
                return False  # invalid character

        return not stack  # stack should be empty if all brackets are balanced
