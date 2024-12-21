// The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 



class Solution {
    public int maxSubArray(int[] nums) {
       int sum=0;
       int maximum=Integer.MIN_VALUE;
       for (int i=0;i<nums.length;i++){

        sum+=nums[i];

        if (sum>maximum){
            maximum=sum;
        }
        if (sum<0){
            sum=0;
        }
       }
       return maximum;

    }
}
