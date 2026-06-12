class Solution:
    # using python function 
    
    # def reverseWords(self, s: str) -> str:
    #     words = s.split()
    #     return " ".join(words[::-1])

    # normal approach
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""

        for ch in s:
            if ch != " ":   
                word += ch
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)

        return " ".join(reversed(words))                       
