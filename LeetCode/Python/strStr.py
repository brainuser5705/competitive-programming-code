class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '' or haystack == needle:
            return 0
        
        needle_len = len(needle)
        
        for i in range((len(haystack)-needle_len)+1):   # add one for to account for indexing
            hay_str = haystack[i:i+needle_len]
            if hay_str == needle:
                return i
            
        return -1