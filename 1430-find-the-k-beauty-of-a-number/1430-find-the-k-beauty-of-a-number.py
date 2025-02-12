class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numst=str(num)
        count=0
        
        cur=int(numst[:k])
        if cur!=0 and num%cur==0:
            count+=1

        for r in range(k,len(numst)):
            cur=int(numst[r-k+1:r+1])
            if cur!=0 and num%cur==0:
                count+=1
        return count    

        