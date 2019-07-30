class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums = sorted(nums)
        closest_val = None
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            while j < k:
                sumup = nums[i] + nums[j] + nums[k]
                if closest_val is None or abs(target - closest_val) > abs(target - sumup):
                    closest_val = sumup
                
                if sumup < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return closest_val