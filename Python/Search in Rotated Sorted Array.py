class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        # binary search -> recursive
        def binarySearch(nums, target, left, right):
            mid = int((left + right) / 2)
            
            if left > right:
                return -1
            
            if nums[mid] == target: # if does not match -> we can then skip the mid position
                return mid
            elif nums[left] <= target < nums[mid]:  # in the left sorted list
                return binarySearch(nums, target, left, mid - 1)
            elif nums[mid] < target <= nums[right]: # in the right sorted list
                return binarySearch(nums, target, mid + 1, right)
            # if neither, should be in the part with pivot -> otherwise there would be no possible match
            elif  nums[mid] > nums[right]:  # pivot on the right
                return binarySearch(nums, target, mid + 1, right)
            else:   # pivot on the left
                return binarySearch(nums, target, left, mid - 1)
                
        
        return binarySearch(nums, target, left, right)
        