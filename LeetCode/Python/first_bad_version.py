# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start = 1
        last = n
        
        # need to pinpoint to one version
        while last != start:
            
            mid = (start + last) // 2
            print('mid: ' mid, end=' ')
            
            if isBadVersion(mid):
                # there must have been a previous bad version
                last = mid - 1
                print('last: ', last, end=' ')
            else:
                # bad version is later
                start = mid + 1
                print('start: ',start, end=' ')
         
        # can also return last
        return start
                