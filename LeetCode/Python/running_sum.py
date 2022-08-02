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

# fastest, in place
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
            
        return nums

# slowest
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        total = nums[0]
        for i in range(1,len(nums)):
            total = total + nums[i]
            nums[i] = total
            
        return nums