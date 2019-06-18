class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        if not nums or target is None:
            return False
        
        def binarySearch(nums, left, right, target):
            if left > right:
                return False
            
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return True
            elif nums[left] < nums[right]:
                if nums[mid] < target:
                    return binarySearch(nums, mid + 1, right, target)
                else:
                    return binarySearch(nums, left, mid - 1, target)
            else:
                if nums[left] == nums[right] == nums[mid]:
                    return binarySearch(nums, left, mid - 1, target) or binarySearch(nums, mid + 1, right, target)
                else:
                    if nums[left] <= nums[mid]:
                        if nums[mid] > target >= nums[left]:
                            return binarySearch(nums, left, mid - 1, target)
                        else:
                            return binarySearch(nums, mid + 1, right, target)
                    else:
                        if nums[mid] < target <= nums[right]:
                            return binarySearch(nums, mid + 1, right, target)
                        else:
                            return binarySearch(nums, left, mid - 1, target)
        
        return binarySearch(nums, 0, len(nums) - 1, target)