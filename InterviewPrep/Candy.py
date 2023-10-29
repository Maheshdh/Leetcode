class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        # compute minimum candies from left to right
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = 1 + candies[i-1]
        # compute overall candies from right to left
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                if candies[i] <= candies[i+1]:
                    candies[i] = 1 + candies[i+1]
        return sum(candies)
            
