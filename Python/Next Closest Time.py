class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        
        digits = set(time[:2] + time[3:])
        original = int(time[:2]) * 60 + int(time[3:])
        min_diff = 2 ** 31 - 1
        ans = None

        # letter combinations + validation
        for a in digits:
            if int(a) > 2:
                continue
            for b in digits:
                if int(a) == 2 and int(b) > 3:
                    continue
                for c in digits:
                    if int(c) > 5:
                        continue
                    for d in digits:
                        this_time = a + b + ':' + c + d
                        temp = int(a + b) * 60 + int(c + d)
                        diff = temp - original

                        # across the day
                        if diff <= 0:
                            diff += 24 * 60
                        if diff < min_diff:
                            ans = this_time
                            min_diff = diff
        return ans