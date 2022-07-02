class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        
        index = -1
        # check if the valid 
        while -index <= len(s) and s[index] != ' ':
            index = index - 1
            
        # add one to move back one iteration
        return -(index+1)