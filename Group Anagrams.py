class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # use sorted characters as key values in hash table
        hash_table = {}
        
        for element in strs:
            sorted_str = ''.join(sorted(element))
            if sorted_str not in hash_table.keys():
                hash_table[sorted_str] = [element]
            else:
                hash_table[sorted_str].append(element)
        return list(hash_table.values())