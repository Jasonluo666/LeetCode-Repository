class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return None
        
        hash_table = {}
        half_len_nums = len(nums) / 2
        
        for num in nums:
            if num in hash_table.keys():
                hash_table[num] += 1
            else:
                hash_table[num] = 1
            
            if hash_table[num] > half_len_nums:
                return num