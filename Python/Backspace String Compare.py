class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def remove_backspace(s):
            index = 0
            while index < len(s):
                if s[index] == '#':
                    s = s[:max(0, index - 1)] + s[index + 1:]
                    index = max(0, index - 1)
                else:
                    index += 1
            return s
        
        if remove_backspace(S) == remove_backspace(T):
            return True
        else:
            return False