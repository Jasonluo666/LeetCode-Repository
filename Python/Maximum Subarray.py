class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return
        
        current_sum = nums[0]
        index = 1
        ans = current_sum
        while index < len(nums):
            new_sum = current_sum + nums[index]
            if new_sum < nums[index]:
                ans = max(ans, current_sum)
                current_sum = nums[index]
            else:
                if new_sum < current_sum:
                    ans = max(ans, current_sum)
                current_sum = new_sum
            index += 1
        return max(ans, current_sum)