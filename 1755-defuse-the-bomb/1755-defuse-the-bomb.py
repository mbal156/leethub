class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:    
        result=[0]*len(code)    
        if k==0:
            return result


        for i in range(len(code)):
            count=0
            if k>0:
                for j in range(1,k+1):
                    count+=code[(i+j)%len(code)]
            
            else :
                for j in range(1,abs(k)+1):
                    count+=code[(i-j)%len(code)]       
            result[i]=count        
        
        return result    
                
                