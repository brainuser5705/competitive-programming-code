class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        prefix = ''
        index = 0
        
        while True:
            
            letter = None
            
            for string in strs:
                
                # Check the length of each string
                if len(string) == index:
                    return prefix
                else:
                    
                    # If it is the first string
                    if letter == None:
                        letter = string[index]
                        
                    # otherwise check if it matches the first string's letter
                    elif letter != string[index]:
                        return prefix
            
            # After going through all the strings
            prefix = prefix + letter
            
            index = index + 1
            
        