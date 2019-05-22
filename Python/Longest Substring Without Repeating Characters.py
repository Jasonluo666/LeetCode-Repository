class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = right = 0
        existence = {}
        ans = 0
        
        while right < len(s):
            if s[right] not in existence or existence[s[right]] is None:
                existence[s[right]] = right
                right += 1
            else:
                ans = max(ans, right - left)
                while left <= existence[s[right]]:
                    existence[s[left]] = None
                    left += 1
        
        ans = max(ans, right - left)
        return ans