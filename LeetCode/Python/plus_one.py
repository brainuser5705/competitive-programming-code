class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # if an extra place is needed
        if digits == []:
            return [1]
        elif digits[-1] == 9:
            return self.plusOne(digits[:-1]) + [0]
        else:
            digits[-1] = digits[-1] + 1
            return digits
        