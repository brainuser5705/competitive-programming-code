class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        arr = [[1]]
        
        for i in range(rowIndex):
            new_arr = [1]
            for j in range(len(arr[-1])-1):
                new_arr += [arr[-1][j] + arr[-1][j+1]]
            new_arr += [1]
            arr.append(new_arr)
        
        return arr[rowIndex]