class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        if n ==0:
            return 0
        totalPossibilities = 1
        i = 0
        while i<n:
            j =i
            while j <n and word[i] == word[j]:
                j +=1

            blockLength = j-i
            if blockLength > 1:
                totalPossibilities += (blockLength -1)
            i =j
        return totalPossibilities