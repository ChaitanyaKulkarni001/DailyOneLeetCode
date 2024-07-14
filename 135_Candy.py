class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 0:
            return 0
        if len(ratings) == 1:
            return 1

        empty_candies = [1] * len(ratings)
        # print(empty_candies)
        
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                empty_candies[i] = empty_candies[i-1]+1

        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                empty_candies[i] = max( empty_candies[i],empty_candies[i+1]+1 )
        return sum(empty_candies)
