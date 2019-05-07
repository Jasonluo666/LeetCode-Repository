# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # simple greedy method
        intervals = sorted(intervals, key=lambda x:x.start)
        
        ans = []
        for element in intervals:
            index = 0
            while index < len(ans) and ans[index] > element.start:
                index += 1
            
            if index == len(ans):
                ans.append(element.end)
            else:
                ans[index] = element.end
        
        return len(ans)