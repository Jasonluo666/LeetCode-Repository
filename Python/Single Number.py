class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        xor_ans = 0
        
        for element in nums:
            xor_ans ^= element
        
        return xor_ans