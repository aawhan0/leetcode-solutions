class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        exp = n
        if exp<0:
            x = 1/x
            exp = -exp
        ans = 1.0
        base = x

        while exp>0:
            if exp &1:
                ans *= base
            base*= base
            exp //= 2
        return ans