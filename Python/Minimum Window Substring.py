class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0:
            return ""
        
        # sliding window -> if satisfy, move the left bondary. otherwise, move the right boundary
        import collections
        counter = collections.Counter(t)
        is_satisfy = False
        min_length = len(s) + 1
        left_bond = right_bond = None
        
        left = right = 0
        while right < len(s):
            counter[s[right]] -= 1

            # whether it contains t -> have to consider multiple same characters
            if counter[s[right]] == 0 and not is_satisfy:
                is_satisfy = max(list(counter.values())) <= 0
            
            while is_satisfy and left <= right:
                counter[s[left]] += 1
                is_satisfy = max(list(counter.values())) <= 0
                
                if not is_satisfy and min_length > right - left + 1:
                    min_length = right - left + 1
                    left_bond = left
                    right_bond = right
                    
                left += 1         
            
            right += 1
        
        if min_length == len(s) + 1:
            return ""
        else:
            return s[left_bond: right_bond + 1]