class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        def binarySearch(nums, left, right, target):
            if left > right:
                return -1
            
            half = int((left + right) / 2)
            if nums[half] < target:
                return binarySearch(nums, half + 1, right, target)
            elif nums[half] == target:
                return half
            else:
                return binarySearch(nums, left, half - 1, target)
        
        index = binarySearch(nums, 0, len(nums) - 1, target)
        if index != -1:
            ans = [index, index]
            for left in range(index - 1, -1, -1):
                if nums[left] == target:
                    ans[0] = left
                else:
                    break
            for right in range(index + 1, len(nums)):
                if nums[right] == target:
                    ans[1] = right
                else:
                    break
            return ans
        
        return [-1, -1]