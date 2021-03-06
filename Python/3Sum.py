class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # O(nlogn + n^2) -> O(n^2)
        sorted_nums = sorted(nums)
        ans = []
        
        # for each element, create double pointers starting from the both sides
        for index in range(len(sorted_nums) - 2):
            # pruning the redundant loop
            if index > 0 and sorted_nums[index - 1] == sorted_nums[index]:
                continue
            if sorted_nums[index] > 0:
                break
            
            left = index + 1
            right = len(sorted_nums) - 1
            flag = True
            while left < right:
                sum = sorted_nums[index] + sorted_nums[left] + sorted_nums[right]
                
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans.append([sorted_nums[index], sorted_nums[left], sorted_nums[right]])
                    # guarantee to be unique
                    while left < right:
                        if sorted_nums[left] == sorted_nums[left + 1]:
                            left += 1
                        elif sorted_nums[right] == sorted_nums[right - 1]:
                            right -= 1
                        else:
                            break
                    left += 1
                    right -= 1
                
        return ans

        
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        from collections import Counter
        
        counter = Counter(nums)
        ans = {}
        
        for i in counter:
            for j in counter:
                k = -i - j
                
                if k in counter:
                    if i == j:
                        if (k == i and counter[i] >= 3) or (k != i and counter[i] >= 2):
                            ans[tuple(sorted([i, j, k]))] = True
                    else:
                        if (k == i and counter[i] >= 2) or (k == j and counter[j] >= 2) or (k != i and k != j):
                            ans[tuple(sorted([i, j, k]))] = True
                            
                            
        return list(ans.keys())
'''