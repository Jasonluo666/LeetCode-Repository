class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left = right = None
        
        for index in range(len(nums)):
            if sorted_nums[index] != nums[index]:
                left = index
                break
        
        for index in range(len(nums) - 1, -1, -1):
            if sorted_nums[index] != nums[index]:
                right = index
                break
        
        if left is None:
            return 0
        else:
            return right - left + 1