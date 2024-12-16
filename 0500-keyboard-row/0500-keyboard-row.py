class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first=set("qwertyuiopQWERTYUIOP")
        second=set("asdfghjklASDFGHJKL")
        third=set("zxcvbnmZXCVBNM")
        
        last=[]
        for word in words:
            word_set=set(word)
            if word_set<=first or word_set<=second or word_set<=third:
                last.append(word)

        return last        



        

            