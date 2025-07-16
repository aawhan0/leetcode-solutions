class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        resArray = []
        for i in range(len(words)):
            if x in words[i]:
                resArray.append(i)
        return resArray
        