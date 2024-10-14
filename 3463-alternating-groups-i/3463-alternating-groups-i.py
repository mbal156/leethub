class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        count=0
        colors+=colors[:2]
        
        for i in range (len(colors)-2):
            
            if colors[i]==colors[i+2] and colors[i] != colors[i+1]:
                    count+=1
                    
                    


                

        # 0 1 0 0 1 0 1
        return count
       