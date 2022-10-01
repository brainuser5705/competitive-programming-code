class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        arr = [[1]]
        
        # special case
        if numRows == 1:
            return arr
        else:
            
            # another special case but kickstarts the iterative process
            if numRows >= 2:
                arr.append([1,1])
            
            # for the rest of the rows
            for i in range(2, numRows):
                
                # use the previous array
                prev_arr = arr[-1]
                
                # add the first one
                new_arr = [1]
                
                # group by two for the sums
                for i in range(len(prev_arr)-1):
                    new_arr.append(prev_arr[i] + prev_arr[i+1])
                
                # add the last one
                new_arr.append(1)
                
                # append the row to the array
                arr.append(new_arr)
                
            return arr