class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # hashmap counter -> ensure 2 distict elements
        hashmap = {}
        left = right = 0
        ans = 0

        # two pointers
        while right < len(s):
            if s[right] not in hashmap:
                if len(hashmap) == 2:
                    # update ans
                    ans = max(ans, right - left)
                    while min(hashmap.values()) > 0:
                        hashmap[s[left]] -= 1
                        left += 1
                    
                    for key in hashmap.keys():
                        if hashmap[key] == 0:
                            del hashmap[key]
                
                hashmap[s[right]] = 1
                    
            else:
                hashmap[s[right]] += 1
            right += 1
        ans = max(ans, right - left)
        return ans