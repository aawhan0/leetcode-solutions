class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # step 1: nums[i] < nums[i+1]
        i = n-2 #second last element
        while i>=0 and nums[i] >= nums[i+1]:
            i-=1

        if i>=0:
            j = n-1 #last element
            while nums[j] <= nums[i]:
                j-=1
            nums[i], nums[j] = nums[j], nums[i]

        #reverse suffix starting at i+1
        left, right = i+1, n-1
        while left < right:
            nums[left] , nums[right] = nums[right], nums[left]
            left +=1
            right -=1