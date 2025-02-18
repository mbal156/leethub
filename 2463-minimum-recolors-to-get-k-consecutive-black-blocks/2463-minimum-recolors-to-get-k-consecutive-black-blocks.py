class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cur = blocks[:k].count("W")  # İlk k karakter içinde kaç tane "w" 
        best = cur 
        
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                cur += 1
            if blocks[i-k] == "W":
                cur -= 1
            
            best = min(best, cur)  
        
        return best




        