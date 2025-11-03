class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        n = len(nums)

        for fast in range(n):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow, n):
            nums[i] = 0
        