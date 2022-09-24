class Solution:
    def climbStairs(self, n: int) -> int:
        
        arr = [1, 2]
        
        if n == 1:
            return arr[0]
        elif n == 2:
            return arr[1]
        else:
            i = 2
            while (i != n):
                arr.append(arr[i-1] + arr[i-2])
                i += 1

            return arr[i-1]