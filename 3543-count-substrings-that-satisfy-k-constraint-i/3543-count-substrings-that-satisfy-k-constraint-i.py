class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count=0
        
        for i in range(len(s)):
            zeros=0
            ones=0
            for j in range(i,len(s)):
                if s[j]=="0":
                    zeros+=1
                elif s[j]=="1":
                    ones+=1
                
                if zeros> k and ones>k:
                    break
                else:
                    count+=1

            
        return count



         


        