# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        
        if not intervals:
            return []
        
        import operator
        intervals = sorted(intervals, key=operator.attrgetter('start'))
        update_pointer = 0
        ans = []
        for index in range(1, len(intervals)):
            if intervals[index].start <= intervals[update_pointer].end:
                intervals[update_pointer].end = max(intervals[update_pointer].end, intervals[index].end)
            else:
                ans.append(intervals[update_pointer])
                update_pointer = index
        
        ans.append(intervals[update_pointer])
        return ansz