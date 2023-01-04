class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # keep a set of the past numbers to see if it cycles back
        
        s = set({n})
        
        while (n != 1):
            
            total = 0
            while n != 0:
                total += (n % 10)**2
                n = n // 10
                
            if total in s:
                break
            else:
                s.add(total)
                n = total
        
        return n == 1