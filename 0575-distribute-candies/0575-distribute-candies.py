from collections import defaultdict
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        flow=defaultdict(int)
        n=len(candyType)
        max_candy=n//2
        for i in range(n):
            num=candyType[i]
            flow[num]+=1

        diff_type=len(flow)

        return min(diff_type,max_candy)

        


        