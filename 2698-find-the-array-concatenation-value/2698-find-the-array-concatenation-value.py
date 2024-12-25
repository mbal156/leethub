class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        sumofcon=0
        while(i<j):
            conval=int(str(nums[i])+str(nums[j]))
            sumofcon+=conval
            i+=1
            j-=1 
        if i==j:
            sumofcon+=nums[i]

        return sumofcon

        
        

            
        