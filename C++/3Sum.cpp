class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        
        
        if(nums.size() < 3)
            return ans;
        
        // sort vector
        sort(nums.begin(), nums.end());
        
        int index = 0;
        int left, right, sum;
        
        while(index < nums.size()){
            if(index > 0 and nums[index] == nums[index - 1]){
                index++;
                continue;
            }
            
            left = index + 1;
            right = nums.size() - 1;
            while(left < right){
                sum = nums[index] + nums[left] + nums[right];
                
                if(sum > 0)
                    right -= 1;
                else if(sum < 0)
                    left += 1;
                else{
                    vector<int> current_ans;
                    current_ans.push_back(nums[index]);
                    current_ans.push_back(nums[left]);
                    current_ans.push_back(nums[right]);
                    ans.push_back(current_ans);
                    
                    while(left < right and nums[left] == current_ans[1])
                        left += 1;
                    while(left < right and nums[right] == current_ans[2])
                        right -= 1;
                }
            }
            
            index++;
        }
        
        return ans;
    }
};