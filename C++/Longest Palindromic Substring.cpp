class Solution {
public:
    string longestPalindrome(string s) {

        // expand every element -> fetch the maximum expansion
        int max_len = 1, pos = 0;
        for(int i = 0, shift = 1, local_max = 1; i < s.length(); i++){
            // odd
            local_max = 1;
            shift = 1;
            while(i - shift >= 0 && i + shift < s.length() && s[i - shift] == s[i + shift]){
                local_max += 2;
                shift++;
            }
            
            if(max_len < local_max){
                max_len = max_len > local_max? max_len: local_max;
                pos = i - shift + 1;
            }
            
            // even
            if(i + 1 < s.length() && s[i + 1] == s[i]){
                local_max = 2;
                shift = 1;
                while(i - shift >= 0 && i + shift + 1 < s.length() && s[i - shift] == s[i + shift + 1]){
                local_max += 2;
                shift++;
            }

                if(max_len < local_max){
                    max_len = max_len > local_max? max_len: local_max;
                    pos = i - shift + 1;
                }
            }
        }
        
        // return substring
        return s.substr(pos, max_len);
    }
};