// In cpp, there is next_permutation function , which automatically solves the problem

class Solution {
    public void nextPermutation(int[] nums) {
        int fall=-1;
        int j=-1;
        for (int i=nums.length-2;i>=0;i--){
            if (nums[i]<nums[i+1]){

                fall = i;
                j=i;
                break;
            }
        }
        fall=j;
        if (j==-1){
             for (int i = 0; i < nums.length / 2; i++) {
            int t = nums[i];
            nums[i] = nums[nums.length - 1 - i];
            nums[nums.length - 1 - i] = t;
            // return nums;
        }
        return;
        }
        

        int mini = fall;
        for (int i=nums.length-1;i>=fall;i--){
            if (nums[i]>nums[fall]){
                mini=i;
                int temp = nums[i];
                nums[i] = nums[fall];
                nums[fall] = temp;
                break;
            }
        }

        // for (int i=mini+1;i<nums.length;i++){
        //      int t = nums[i];
        //     nums[i] = nums[nums.length - 1 - i];
        //     nums[nums.length - 1 - i] = t;
        //     // return nums;
        // }

        int start = fall + 1, end = nums.length - 1;
        while (start < end) {  // Fixed: Corrected the reverse logic
            int t = nums[start];
            nums[start] = nums[end];
            nums[end] = t;
            start++;
            end--;
        }


        }

    }
