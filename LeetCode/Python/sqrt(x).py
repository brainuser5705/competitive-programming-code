class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        i = 0
        while i*i <= x: # go beyond the square, or until square is exceeded
            i += 1
            
        return i-1 
        