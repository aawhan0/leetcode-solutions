class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        ctr = 0

        for i in range(n):
            if nums[i] > nums[(i+1)%n]:
                ctr += 1
            if ctr >1:
                return False
        return True