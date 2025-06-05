class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
          if (nums.size() == 0){
            return {-1,-1};
        }

        auto front = find(nums.begin(), nums.end(), target);
        if (front == nums.end()) {
            return {-1, -1};
        }
        int start = distance(nums.begin(), front);
        reverse(nums.begin(),nums.end());
        auto back = find(nums.begin(), nums.end(), target);
        int end = nums.size()- distance(nums.begin(),back)-1;

        vector<int> ans = {start, end};
        return ans;
    }
};
