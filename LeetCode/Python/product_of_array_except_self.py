class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        arr1 = [1]
        for i in range(0, len(nums)):
            arr1.append(arr1[i]*nums[i])

        arr2 = [1]
        for i in range(len(nums)-1,0,-1):
            arr2.insert(0,arr2[0
            ]*nums[i])

        final = []
        for i in range(len(nums)):
            final.append(arr1[i] * arr2[i])

        return final

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        arr1 = [1]
        for i in range(0, len(nums)-1):
            arr1.append(arr1[i]*nums[i])

        prev = 1
        for i in range(len(nums)-1,0,-1): 
            prev *= nums[i]
            arr1[i-1] *= prev

        return arr1