class Solution {
private:
    void dfs(vector<string>& ans, string str, int left, int right) {
        if(left == 0 and right == 0)
            ans.push_back(str);
        
        if(left > 0)
            dfs(ans, str + "(", left - 1, right);
        if(right > left)
            dfs(ans, str + ")", left, right - 1);
    }
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;

        // recursively create string
        dfs(ans, "", n, n);
        
        return ans;
    }
};