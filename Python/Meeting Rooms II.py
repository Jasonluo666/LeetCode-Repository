# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        ans = []
        for interval in sorted_intervals:
            index = 0
            while index < len(ans):
                if ans[index] <= interval[0]:
                    ans[index] = interval[1]
                    break
                index += 1
            
            if index == len(ans):
                ans.append(interval[1])
        return len(ans)