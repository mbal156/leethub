class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        sumofcon=[]
        while(i<j):
            conval=int(str(nums[i])+str(nums[j]))   
            sumofcon.append(conval)
            i+=1
            j-=1 
        if i==j:
            return sum(sumofcon)+nums[i]
        return sum(sumofcon)        

        

        
        

            
        