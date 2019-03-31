class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if len(nums) == 0:
            return ans
        
        # update max index only if it's outdated
        max_index = -1
        for index in range(k - 1, len(nums)):
            if max_index >= 0 and nums[index] >= nums[max_index]:
                max_index = index
            
            if max_index == index - k:
                max_index += 1
                for pointer in range(index - k + 1, index + 1):
                    if nums[pointer] >= nums[max_index]:
                        max_index = pointer
            ans.append(nums[max_index])
        
        return ans