class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums) - 1
        check_list = [False for x in range(n + 1)]
        
        ans = None
        for element in nums:
            if check_list[element] == False:
                check_list[element] = True
            else:
                ans = element
                break
        
        return ans