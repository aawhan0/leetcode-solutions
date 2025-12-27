class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 
        }

        total = 0 #initialising the output
        n = len(s) # s is the input string

        for i in range(n):
            v = values[s[i]] #ith index element in s string

            if i+1 <n and v< values[s[i+1]]:
                total -= v
            else:
                total += v
            
        return total
