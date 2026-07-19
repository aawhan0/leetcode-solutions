class Solution:
    def isValid(self, s: str) -> bool: #s means string
        stack = []
        mapper = {")" : "(",
                  "]" : "[",
                  "}" : "{"
                }

        for i in s:

            if i in mapper: #is the current character a closing bracket? -> yes, then 
                if not stack or stack[-1] != mapper[i]: #stack[-1] is the top element of stack.
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0

