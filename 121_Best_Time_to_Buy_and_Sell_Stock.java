// Dynamic approach, remembering the past

class Solution {
    public int maxProfit(int[] prices) {
        // Oprimal Approach 
        
        int small = prices[0];
        int profit =0;
        int cost=0;
        for (int i=1;i<prices.length;i++){
            cost = prices[i] - small;

            profit = Math.max(profit,cost);

            small = Math.min(small,prices[i]);
        }
        return profit;
    }
}
