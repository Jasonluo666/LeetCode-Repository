class Solution {
private:
    int dfs(vector<int>& nums, int target, int left, int right){
        if(left > right)
            return -1;
        
        int mid = (int) ((left + right) / 2);
        
        if(nums[mid] == target)
            return mid;
        else if(nums[left] <= target and target < nums[mid])
            return dfs(nums, target, left, mid - 1);
        else if(nums[mid] < target and target <= nums[right])
            return dfs(nums, target, mid + 1, right);
        else if(nums[left] > nums[mid])
            return dfs(nums, target, left, mid - 1);
        else
            return dfs(nums, target, mid + 1, right);
    }
public:
    int search(vector<int>& nums, int target) {
        return dfs(nums, target, 0, nums.size() - 1);
    }
};