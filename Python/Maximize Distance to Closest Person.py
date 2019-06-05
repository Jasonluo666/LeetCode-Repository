class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        
        left_person = False
        counter = 0
        ans = 0
        for seat in seats:
            if seat == 0:
                counter += 1
            elif left_person == False:
                left_person = True
                ans = counter
                counter = 0
            else:
                ans = max(ans, int((counter + 1) / 2))
                counter = 0
        ans = max(ans, counter)
        
        return ans