class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        resArray = [] # creating an empty array which is gonna be returned
        length = len(words) 
        for i in range(length):
            if x in words[i]:
                resArray.append(i)
        return resArray
        