class Solution {
    public void sortColors(int[] nums) {
        int low=0;
        int mid=0;
        int high =nums.length-1;
    while(mid<=high){

        if (nums[mid] == 1){
            mid++;
        }
        else if (nums[mid]==0){
            if (mid!=low){

            nums[low]=0;
            nums[mid]=1;
            low++;mid++;
            }
            else{
                nums[low]=0;
                low++;
                mid++;
            }
        }
        else{
            int temp = nums[mid];
            nums[mid] = nums[high];
            nums[high] = temp;
            high--;
        }
    }

    }
}
