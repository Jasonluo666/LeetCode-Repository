class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        ans = [[]]
        if not nums:
            return [[]]
        else:
            unique_element = list(set(nums))
        
        # to generate the subset, we iteratively construct the subset list
        for element in unique_element:
            new_ans = []
            for result in ans:
                new_ans.append(result + [element])
            ans += new_ans.copy()
        
        return ans