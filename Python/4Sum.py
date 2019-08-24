class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums = sorted(nums)
        ans = []
        
        for left in range(len(nums) - 3):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            
            right = len(nums) - 1
            while right - left > 2:
                i, j = left + 1, right - 1
                while i < j:
                    sumup = nums[i] + nums[j] + nums[left] + nums[right]

                    if sumup == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                    if sumup < target:
                        i += 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                    else:
                        j -= 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
                
                right -= 1
                while right - left > 2 and nums[right] == nums[right + 1]:
                    right -= 1
        return ans