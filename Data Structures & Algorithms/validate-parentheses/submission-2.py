class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ifmatch = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in ifmatch:
                if stack and stack[-1] == ifmatch[c]:
                    stack.pop()
                else:
                    stack.append(c)
            else: 
                stack.append(c)
        
        if stack:
            return False
        else: 
            return True

        