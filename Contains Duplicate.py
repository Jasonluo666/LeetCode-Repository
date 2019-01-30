class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # easy peasy
        is_duplicate = False
        hash_table = {}
        for element in nums:
            if element not in hash_table.keys():
                hash_table[element] = True
            else:
                is_duplicate = True
                break
        
        if is_duplicate:
            return True
        else:
            return False