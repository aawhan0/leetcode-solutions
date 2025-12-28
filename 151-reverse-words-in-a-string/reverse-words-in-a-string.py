class Solution:
    def reverseWords(self, s: str) -> str:
        words= []
        i= 0
        n= len(s)
    
        while i<n:
            while i<n and s[i] == " ":
                # = means asign op and == means equal to
                i+= 1
            if i<n:
                j = i
                while j<n and s[j] != " ":
                    j += 1
                words.append(s[i:j])
                i = j
        return ' '.join(words[::-1])
        