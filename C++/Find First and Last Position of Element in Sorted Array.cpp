class Solution {
private:
    // binary search for sorted array
    int binarySearch(vector<int>& nums, int target, int left, int right){
        if(left > right)
            return -1;
        
        int mid = (int) ((left + right) / 2);
        
        if(nums[mid] == target)
            return mid;
        else if(nums[mid] > target)
            return binarySearch(nums, target, left, mid - 1);
        else
            return binarySearch(nums, target, mid + 1, right);
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ans;
        
        int pos = binarySearch(nums, target, 0, nums.size() - 1);
        
        if(pos == -1){
            ans.push_back(-1);
            ans.push_back(-1);
        }
        else{
            // find the boundary of target value
            int left = 0, right = 0;
            while(pos - left >= 0 and nums[pos - left] == target)
                left++;
            
            while(pos + right < nums.size() and nums[pos + right] == target)
                right++;
            
            ans.push_back(pos - left + 1);
            ans.push_back(pos + right - 1);
        }
        
        
        return ans;
    }
};