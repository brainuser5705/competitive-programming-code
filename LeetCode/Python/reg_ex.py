class Solution(object):
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if not p:
            return not s
        
        # match single char if no *
        match = bool(s) and p[0] in {s[0], '.'} 
        
        if len(p)>= 2 and p[1] == '*':
            return (
                self.isMatch(s,p[2:])  # zero chars - skip
                or
                (match and self.isMatch(s[1:],p)) # match more than one char
            ) 
        else:
            return match and self.isMatch(s[1:], p[1:])   # only one char match