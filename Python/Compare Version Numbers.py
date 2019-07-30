class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
        if not version1 or not version2:
            return 0
        
        ans = 0
        while len(version1) > 0 and len(version2) > 0:
            i, j = version1.find('.'), version2.find('.')
            if i == -1:
                i = len(version1)
            if j == -1:
                j = len(version2)
            
            num1, num2 = int(version1[:i]), int(version2[:j])
            version1 = version1[i + 1:]
            version2 = version2[j + 1:]
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        
        if not version1 and not version2:
            return 0
        elif not version1:
            for element in version2:
                if element != '0' and element != '.':
                    return -1
            return 0
                
        else:
            for element in version1:
                if element != '0' and element != '.':
                    return 1
            return 0
            return 1