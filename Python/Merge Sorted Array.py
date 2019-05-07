class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        pointer1, pointer2, current = m - 1, n - 1, m + n - 1
        
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] > nums2[pointer2]:
                nums1[current] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[current] = nums2[pointer2]
                pointer2 -= 1
            current -= 1
        
        while pointer2 >= 0:
            nums1[current] = nums2[pointer2]
            pointer2 -= 1
            current -= 1
        