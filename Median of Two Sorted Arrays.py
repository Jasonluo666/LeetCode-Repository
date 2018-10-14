class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # using the characterastics of median

        # nums1 <= nums2
        len1, len2 = len(nums1), len(nums2)
        half = int((len1 + len2 + 1) / 2)
        if len1 > len2:
            nums1, nums2 = nums2, nums1
            len1, len2 = len2, len1
        
        imin, imax = 0, len1
        while True:
            pointer_x = int(imin + imax / 2)
            pointer_y = half - pointer_x
            
            if pointer_x < len1 and nums1[pointer_x] < nums2[pointer_y - 1]:
                imin += 1
            elif pointer_x > 0 and nums1[pointer_x - 1] > nums2[pointer_y]:
                imax -= 1
            else:
                if pointer_x == 0:
                    left_max = nums2[pointer_y - 1]
                elif pointer_y == 0:
                    left_max = nums1[pointer_x - 1]
                else:
                    left_max = max(nums1[pointer_x - 1], nums2[pointer_y - 1])
                
                if (len1 + len2) % 2 == 1:
                    return left_max
                
                if pointer_x == len1:
                    right_min = nums2[pointer_y]
                elif pointer_y == len2:
                    right_min = nums1[pointer_x]
                else:
                    right_min = min(nums1[pointer_x], nums2[pointer_y])
                
                return (left_max + right_min) / 2