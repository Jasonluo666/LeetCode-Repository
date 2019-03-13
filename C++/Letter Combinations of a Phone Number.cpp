class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        if(digits.length() == 0)
            return ans;
        
        ans.push_back("");
        string str[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        
        // renew the combination result for every iteration
        // append new character to the tail
        for(int i = 0; i < digits.length(); i++){
            vector<string> new_ans;
            
            string alternative = str[digits[i] - '0' - 2];
            for(int j = 0; j < alternative.length(); j++)
                for(int k = 0; k < ans.size(); k++)
                    new_ans.push_back(ans[k] + alternative[j]);
            
            ans = new_ans;
        }
        
        return ans;
    }
};