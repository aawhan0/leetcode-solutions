class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count= maxcount =0
        for num in nums:
            count = count + 1 if num ==1 else 0
            maxcount = max(count, maxcount)
        return maxcount