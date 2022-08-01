class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        arr = []
        _sum = 0
        for num in nums:
            _sum = _sum + num
            arr.append(_sum)
            
        return arr