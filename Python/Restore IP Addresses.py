class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # dfs thru all valid results
        ans = []
        def possibleAns(s, current_ip, index):
            if index == 4 or len(s) == 0:
                if index == 4 and len(s) == 0:
                    ans.append(current_ip[:-1])
                return
            
            possible_num = ''
            for pos in range(len(s)):
                possible_num += s[pos]
                if int(possible_num) <= 255 and not (len(possible_num) > 1 and possible_num[0] == '0'):
                    possibleAns(s[pos + 1:], current_ip + possible_num + '.', index + 1)
                else:
                    break
            return
        
        possibleAns(s, '', 0)
        return ans
    