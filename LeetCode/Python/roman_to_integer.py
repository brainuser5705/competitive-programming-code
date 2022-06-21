class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sum = 0
        
        i = 0
        
        while i < len(s):
            
            letter = s[i]
            
            if letter == 'I':
                if i + 1 != len(s) and s[i+1] == 'V':
                    sum = sum + 4
                    i = i + 1
                elif i + 1 != len(s) and s[i+1] == 'X':
                    sum = sum + 9
                    i = i + 1
                else:
                    sum = sum + 1
            elif letter == 'V':
                sum = sum + 5
            elif letter == 'X':
                if i + 1 != len(s) and s[i+1] == 'L':
                    sum = sum + 40
                    i = i + 1
                elif i + 1 != len(s) and s[i+1] == 'C':
                    sum = sum + 90
                    i = i + 1
                else:
                    sum = sum + 10
            elif letter == 'L':
                sum = sum + 50
            elif letter == 'C':
                if i + 1 != len(s) and s[i+1] == 'D':
                    sum = sum + 400
                    i = i + 1
                elif i + 1 != len(s) and s[i+1] == 'M':
                    sum = sum + 900
                    i = i + 1
                else:
                    sum = sum + 100
            elif letter == 'D':
                sum = sum + 500
            elif letter == 'M':
                sum = sum + 1000
                
            i+=1
            
        return sum


## recursive version w. dictionary

class Solution(object):
    
    def __init__(self):
        self.values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        return self.get_integer(s, 0, '')
        
    
    def get_integer(self, s, total, lc):
        
        if s == '':
            return total
        else:
            
            letter = s[0]
            value = self.values[letter]
            
            # not subtracting 1, 10, 100 since the previous value already got added
            if lc == 'I' and (letter == 'V' or letter == 'X'):
                value = value - 2   
            elif lc == 'X' and (letter == 'L' or letter == 'C'):
                value = value - 20
            elif lc == 'C' and (letter == 'D' or letter == 'M'):
                value = value - 200
                
            total = total + value
            
            return self.get_integer(s[1:], total, letter)
            