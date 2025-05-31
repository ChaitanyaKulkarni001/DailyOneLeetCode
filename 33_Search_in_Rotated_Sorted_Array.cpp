class Solution {
public:
    int search(vector<int>& nums, int target) {
         
          int low = 0;
        int high = nums.size()-1;

        while (low<=high){

            int mid = (low + high)/2;
            // cout << "Current Mid is " << mid << " LOW "<< low << " high " << high << endl ;
            if (target == nums[mid] ){
                // cout << nums[mid] << " at " << mid <<endl;
                return mid;
            }
           
            if (nums[low]<=nums[mid]){
                // Low is sorted
                // cout << " In the Left at low " << low << " and high "<< high << " Mid is "<< mid << " Current Num " << nums[mid] << endl;
                if (nums[low]<= target && target < nums[mid]){
                    high = mid - 1;
                    cout << " HERE";
                }
                else{
                    low = mid + 1;
                }
            }
            else{
                // High is sorted
                 if (nums[mid]< target && target <= nums[high]){
                    low = mid + 1;
                }
                else{
                    high = mid - 1;
                }
            }

        }
        return -1;


    }
};
