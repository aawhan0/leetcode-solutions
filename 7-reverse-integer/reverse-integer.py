class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2**31 -1
        int_min = -2**31

        sign =-1 if x<0 else 1
        x = abs(x)
        rev = 0

        while x!=0:
            ld = x% 10
            x//= 10

            if rev> (int_max - ld)//10:
                return 0
            
            rev = rev*10 +ld

        return sign* rev


