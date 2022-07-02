class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        d = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        
        stack = []
        
        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif stack.pop() != d[char]:
                    return False
                
        return len(stack) == 0