class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        full_w = ''
        
        # convert the string into desired format
        for w in s:
            for c in w:
                if c.isalpha() or c.isnumeric():
                    full_w += c.lower()
        
        # check if palindrome
        for i in range(len(full_w)//2):
            
            if full_w[i] != full_w[-1-i]:
                return False
    
            
        return True