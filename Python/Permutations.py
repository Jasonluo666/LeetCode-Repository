class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # initialize the answer list with only one element
        ans = []
        for num in nums:
            ans.append([num])
        
        for _ in range(len(nums) - 1):
            # every iteration -> append a new element
            # combination task
            current = []
            for element in ans:
                for num in nums:
                    if num not in element:
                        current.append(element + [num])
            ans = current.copy()
        
        return ans