class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        from collections import Counter
        counter = Counter(p)
        tail = 0
        while tail < len(p) and tail < len(s):
            if s[tail] in counter:
                counter[s[tail]] -= 1
            tail += 1
        
        head = 0
        ans = []
        while True:
            if max(counter.values()) == 0:
                ans.append(head)
            
            if tail == len(s):
                break
            
            if s[tail] in counter:
                counter[s[tail]] -= 1
            tail += 1
                
            if s[head] in counter:
                counter[s[head]] += 1
            head += 1
        return ans