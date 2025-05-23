class Solution {
    public int[] rearrangeArray(int[] nums) {
        // Optimal Approach 

        int pos=0;
        int neg=1;
        int[] arr = new int[nums.length];
        for (int i=0;i<nums.length;i++){
            if (nums[i]>0){
                arr[pos] = nums[i];
                pos= pos+2;
            }
            else{
                arr[neg] = nums[i];
                neg=neg+2;
            }
        }
        return arr;

        // Brute Force Approach        
        int len = nums.length;
        int[] pos = new int[len/2];
        int[] neg = new int[len/2];
        int turnP=1;
        int num_i = 0;
        int num_j =0 ;
        for (int i=0;i<len;i++){
            if (nums[i]>0){
                pos[num_i] = nums[i];
                num_i++;
            }
            else{
                neg[num_j] = nums[i];
                num_j++;
            }
        }
        num_i=0;
        num_j=0;
        for (int i=0;i<len;i++){
            if(turnP==1){
            nums[i] = pos[num_i];
            turnP--;  
            num_i++;
            }
            else{
                nums[i] = neg[num_j];
                turnP++;
                num_j++;
            }

        }
        return nums;


        



    }
}
