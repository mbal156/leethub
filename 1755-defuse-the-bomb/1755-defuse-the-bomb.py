class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:    
        elist=[]    
        if k==0:
            return [0]*len(code)


        for i in range(len(code)):
            count=0
            if k>0:
                for j in range(1,k+1):
                    count+=code[(i+j)%len(code)]
            
            else :
                for j in range(1,abs(k)+1):
                    count+=code[(i-j)%len(code)]       
            elist.append(count)        
        
        return elist  
                
                