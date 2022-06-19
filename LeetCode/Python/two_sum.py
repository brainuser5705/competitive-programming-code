# O(n) solution

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # put numbers into dictionary with index
        d = {}
        for index, num in enumerate(nums):
            d[num] = index
        
        # loop through the numbers and see if the difference
        # is in the dictionary and get the index
        # (the difference must not have the same index)
        for index, num in enumerate(nums):
            diff = target - num
            if diff in d.keys() and index != d[diff]:
                return [index, d[diff]]