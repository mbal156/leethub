class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k=nums.count(1)
        nums+=nums
        zeroc=nums[:k].count(0)
        minsw=zeroc
        for i in range(1,len(nums)//2):

            if nums[i-1]==0:
                zeroc-=1
            if nums[i+k-1]==0:
                zeroc+=1
            minsw=min(minsw,zeroc)

        return minsw    


                


                




        