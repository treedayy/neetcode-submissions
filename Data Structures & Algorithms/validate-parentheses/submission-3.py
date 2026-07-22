class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        if (len(s) % 2 != 0):
            return False
        elif (len(s) == 0):
            return True
        elif (s is None):
            return True
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        