class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        while pow(4,i) <= n:
            if pow(4,i) ==n:
                return True
            i += 1
        return False