class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1
        
        def binarySearch(nums, target, left, right):
            if left > right:
                return -1
            
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[right]:
                if nums[mid] < target:
                    return binarySearch(nums, target, mid + 1, right)
                else:
                    return binarySearch(nums, target, left, mid - 1)
            else:
                if nums[mid] < target:
                    if target <= nums[right]:
                        return binarySearch(nums, target, mid + 1, right)
                    else:
                        if nums[mid] >= nums[left]:
                            return binarySearch(nums, target, mid + 1, right)
                        else:
                            return binarySearch(nums, target, left, mid - 1)
                else:
                    if nums[mid] <= nums[right]:
                        return binarySearch(nums, target, left, mid - 1)
                    else:
                        if target <= nums[right]:
                            return binarySearch(nums, target, mid + 1, right)
                        else:
                            return binarySearch(nums, target, left, mid - 1)
        
        return binarySearch(nums, target, 0, len(nums) - 1)