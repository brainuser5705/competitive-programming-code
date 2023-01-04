class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        
        if columnNumber <= 26:
            return chr(64 + columnNumber)
        else:
            val = columnNumber % 26
            
            # numbers actually divisible by 26 will yield in 0....
            # converts number - 1 and edits the last character at the end
            if val == 0:
                name = self.convertToTitle(columnNumber-1)
                return name[:-1] + chr(ord(name[-1])+1)
            else: 
                return self.convertToTitle(columnNumber // 26) + chr(64 + val)