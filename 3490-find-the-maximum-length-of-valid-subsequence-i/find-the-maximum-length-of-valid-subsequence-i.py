class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odds = sum(x&1 for x in nums)
        evens = len(nums) - odds
        flips = sum(a&1 ^ b&1 for a, b in pairwise(nums))

        return max(odds, evens, flips+1)