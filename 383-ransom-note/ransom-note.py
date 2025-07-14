class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = {}
        for c in ransomNote:
           counter[c] = counter.get(c, 0) + 1
        
        for c in magazine:
           if counter.get(c, 0) != 0:
              counter[c] -= 1
        
        return sum(counter.values()) == 0
        


        