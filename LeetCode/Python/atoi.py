class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.lstrip(' ')
        
        sign = '+'
        if len(s) > 1 and s[0] in '-+':
            sign = s[0]
            s = s[1:]
        
        num = ''
        for char in s:
            if char.isdigit():
                num += char
            else:
                 break
                
        if num == '':
            num = 0
        else:
            num = int(sign + num)
            
        if num < -(2**31):
            num = -(2**31)
        elif num > (2**31)-1:
            num = (2**31)-1
            
        return num
            
        
            
            
            
        
        