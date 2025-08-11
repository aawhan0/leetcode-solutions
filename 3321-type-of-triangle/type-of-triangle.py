from typing import List

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums

        # First check if it's a valid triangle
        if a + b <= c or b + c <= a or c + a <= b:
            return "none"

        # All sides equal
        if a == b == c:
            return "equilateral"

        # Any two sides equal
        if a == b or b == c or a == c:
            return "isosceles"

        # All sides different
        return "scalene"
