class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // create hash map in C++
        map<char, bool> hash_map;
        int max_count = 0, current_count = 0, start_pos = 0;

        // visit the string once -> pick the largest substring
        for(int i = 0; i < s.length(); i++){
            if (hash_map.find(s[i]) == hash_map.end() || hash_map[s[i]] == false)
                hash_map[s[i]] = true;
            else{
                if (current_count > max_count)
                    max_count = current_count;
                
                do {
                    hash_map[s[start_pos]] = false;
                    current_count -= 1;
                } while(s[start_pos++] != s[i]);
                
                hash_map[s[i]] = true;
            }
            
            current_count += 1;
        }
        
        return max_count > current_count ? max_count : current_count;
    }
};