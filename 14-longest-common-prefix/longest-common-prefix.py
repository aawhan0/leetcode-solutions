class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        base = strs[0]
        for i in range(len(base)):
            for string in strs[1:]:
                # Check if index i is out of bounds OR characters do not match
                if i == len(string) or string[i] != base[i]:
                    return base[:i]
        
        return base
