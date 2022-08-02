class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        d = {}
        for i in range(len(s)):
            sc = s[i]
            tc = t[i]
            if sc not in d:
                if tc not in d.values():
                    d[sc] = tc
                else:
                    return False
            else:
                if d[sc] != tc:
                    return False
                
        return True