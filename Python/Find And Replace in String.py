class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        shift = 0
        hashmap = {}
        for i, index in enumerate(indexes):
            hashmap[index] = (sources[i], targets[i])
        
        for index in sorted(indexes):
            source, target = hashmap[index]
            index += shift
            
            if S[index: index + len(source)] == source:
                S = S[:index] + target + S[index + len(source):]
                shift += len(target) - len(source)
        
        return S