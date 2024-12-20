class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        map<int,int> storage;

        for(int i=0;i<nums.size();i++){
            int rem = target-nums[i];

            if(storage.find(rem)!=storage.end()){
                return  {i,storage[rem]};
            }
            storage[nums[i]] = i;
        }

        return {-1,-1};    
}
};
