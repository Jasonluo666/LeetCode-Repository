class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        S = ''.join(S.split('-')).upper()
        
        index = len(S) - 1
        count = 0
        while index > 0:
            count += 1
            if count == K:
                S = S[:index] + '-' + S[index:]
                count = 0
            
            index -= 1
        
        return S