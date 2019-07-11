class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        for index in range(len(nums)):
            jump = abs(nums[index])
            while nums[jump - 1] > 0:
                nums[jump - 1] = -nums[jump - 1]
                jump = abs(nums[jump - 1])
        
        ans = []
        for index in range(len(nums)):
            if nums[index] > 0:
                ans.append(index + 1)
        return ans