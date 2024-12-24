class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        h=0
        n=0
        
        
        while h<len(haystack):
            
            if haystack[h]==needle[n]:
                n+=1
                if n==len(needle):   
                    return h-n+1
            
            else:
                h=h-n
                n=0
            
            h+=1                    
        

        ababc
        ab