class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        mid = len(nums) // 2
        
        num = nums[mid]
        if num == target:
            return mid
        elif num < target:
            if nums[mid+1:] == []:
                return mid+1
            # adding (mid+1) to account for the index reset
            return (mid+1) + self.searchInsert(nums[mid+1:], target)
        elif num > target:
            if nums[:mid] == []:
                return mid  # replace the index
            return self.searchInsert(nums[:mid], target)
            
            