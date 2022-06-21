class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        self.check_expr(s, p, ' ')
        
        
        
    def check_expr(self, s, p, lc):
        
        if s == '':
            return True
        elif p == '':
            self.check_expr(s[1:], '', lc)
        elif s[0] == p[0]:
            self.check_expr(s[1:], p[1:], s[0])
        elif p[0] == '.':
            self.check_expr(s[1:], p[1:], '.')
        elif p[0] == '*' and (s[0] == lc or lc == '.'):
            self.check_expr(s[1:], p[1:])
        else:
            return False
        