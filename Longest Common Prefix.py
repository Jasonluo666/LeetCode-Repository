class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # len(strs) == 0
        if not strs:
            return ''
        
        longest_index = 0
        shortest_word = min([len(x) for x in strs])
        
        # stop at the end of the shortest word
        for index in range(shortest_word):
            word = strs[0][index]
                    
            if sum([element[index] == word for element in strs]) == len(strs):
                longest_index += 1
            else:
                break
        
        return strs[0][:longest_index]