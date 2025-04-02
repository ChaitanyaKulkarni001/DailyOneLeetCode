class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefix_count;
        int sum = 0;
        int result = 0;
        prefix_count[0] = 1;
        for (const auto num : nums) {
            sum += num;
            result += prefix_count[sum - k];
            ++prefix_count[sum];
        }
        return result;
    }
};
