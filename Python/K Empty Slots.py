class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        
        if not flowers:
            return -1
        
        # convert to pos[day]
        flip = {}
        for index, pos in enumerate(flowers):
            flip[pos] = index + 1
        
        # two pointers -> i scans from left to right
        left = i = 1
        right = k + i + 1
        ans = len(flip) + 1
        
        while right <= len(flip):
            if flip[i] < flip[left] or flip[i] <= flip[right]:
                # update the minimal ans here (if required)
                if i == right:
                    ans = min(ans, max(flip[left], flip[right]))
                left = i
                right = k + i + 1
            i += 1
        
        if ans == len(flip) + 1:
            return -1
        else:
            return ans