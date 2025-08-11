class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        total = 0
        for i, digit in enumerate(digits):
            val = int(digit)
            if i%2 ==0:
                total = total + val
            else:
                total = total - val
        return total