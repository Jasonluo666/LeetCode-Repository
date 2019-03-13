class Solution {
public:
    int maxArea(vector<int>& height) {
        if(height.size() < 2)
            return 0;
        
        // greedy method
        int left = 0, right = height.size() - 1;
        int max_vol = 0, current_vol;
        while(left < right){
            // always determined by the shorest side
            current_vol = min(height[left], height[right]) * (right - left);
            
            max_vol = max(max_vol, current_vol);
            

            // does not matter if left == right, cuz either part will make no contribution later on
            if(height[left] < height[right])
                left += 1;
            else
                right -= 1;
        }
        
        return max_vol;
    }
};