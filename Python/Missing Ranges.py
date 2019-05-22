class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        
        # special cases
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
        
        # similar to twp pointer operation
        prev = lower - 1
        ans = []
        for element in nums + [upper + 1]:
            diff = element - prev
            if diff > 1:
                if diff == 2:
                    ans.append(str(element - 1))
                else:
                    ans.append(str(prev + 1) + '->' + str(element - 1))
            prev = element
        return ans