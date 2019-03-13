class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # use the hash table/counter -> get frequency of element
        # more efficient than two loops
        import collections
        
        hash_table = collections.Counter(nums2)
        
        ans = []
        for x in nums1:
            if x in hash_table.keys() and hash_table[x] > 0:
                ans.append(x)
                hash_table[x] -= 1
        
        return ans