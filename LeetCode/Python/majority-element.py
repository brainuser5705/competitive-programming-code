class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maj_count = len(nums)//2
        
        nums = sorted(nums)
        print(nums)
        
        count = 1
        i =  0 # initialization
        for i in range(len(nums)-1):
            
            if count > maj_count:
                break
            elif nums[i] == nums[i+1]:
                count += 1
            else:
                count = 1
                
        return nums[i]
            
            
                
        
                
        
        
        