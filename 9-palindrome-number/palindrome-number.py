class Solution:
    def isPalindrome(self, x: int) -> bool:
        # int_max = 2**31 -1
        # int_min = -2**31
        # no need because overflow aint happening here.

        if x<0:
            return False
        original = x
        rev = 0

        while x!= 0:
            ld = x% 10
            rev = rev*10 + ld
            x//= 10
        
        return original == rev