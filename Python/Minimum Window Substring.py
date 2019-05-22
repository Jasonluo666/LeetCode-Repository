class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        import collections
        hashmap = collections.Counter(t)
        ans = ""
        ans_length = len(s) + 1
        left = right = 0
        
        while right < len(s):
            if s[right] in hashmap:
                hashmap[s[right]] -= 1
                
                if max(hashmap.values()) == 0:
                    while left <= right:
                        if s[left] in t:
                            hashmap[s[left]] += 1
                            if hashmap[s[left]] > 0:
                                length = right - left + 1
                                if length < ans_length:
                                    ans_length = length
                                    ans = s[left:right + 1]
                                
                                left += 1
                                break
                        left += 1
            right += 1
        
        return ans