class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d = {}
        # get the number of occurences for each letter in the string
        for l in s:
            if l not in d:
                d[l] = 1
            else:
                d[l] += 1
                
        count = 0
        odd = False
        for l in d:
            # if odd, then only minus 1 of the letters can be used
            if (d[l] % 2 == 1):
                count += d[l] - 1
                # add the extra letter if one hasn't already been added
                if not odd:
                    count += 1
                    odd = True  # can't add any more single letters otherwise it won't be a palindrome
            # if even, then add all the occurrences
            elif (d[l] % 2 == 0):
                count += d[l]
        
        return count