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

arr = [1,2]

for i in range(2,n):
    arr.append(arr[i-1],arr[i-2])

return arr[n-1]


a, b = 1, 1
for _ in range(1,n):
    a, b = b, a + b
return b