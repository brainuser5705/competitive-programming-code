class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        for i in range(len(height)):
            for j in range(i):

                h = min(height[i], height[j])
                max_area = max(max_area, h * (i-j))

        return max_area

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height)-1

        a = 0

        while i != j:

            i_height = height[i]
            j_height = height[j]

            a = max(a, min(i_height, j_height) * (j-i))

            if i_height < j_height:
                i += 1
            else:
                j -= 1

        return a