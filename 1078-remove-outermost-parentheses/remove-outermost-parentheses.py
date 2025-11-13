class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        counter = 0
        for i in s:
            if i == '(':
                if counter != 0:
                    result.append(i)
                counter += 1
            else: # i == ')'
                counter -= 1
                if counter != 0:
                    result.append(i)
        return ''.join(result) #'' mean there is no seperators between characters