class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) > len(t):
            return False
        
        s_index = 0
            
        for c in t:
            if s_index == len(s):
                return True
            elif c == s[s_index]:
                s_index = s_index + 1
            
        return s_index == len(s) # if last character of t was end of subsequence s