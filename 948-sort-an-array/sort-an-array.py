class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums)//2

        left_nums = nums[: mid]
        right_nums = nums[mid :]

        #recursions:
        left_nums = self.sortArray(left_nums)
        right_nums = self.sortArray(right_nums)

        #merge
        i = j = k = 0 
        # i is the leftmost index of left_nums
        # j is the leftmost index of the right_nums

        while i<len(left_nums) and j<len(right_nums):
            if left_nums[i] < right_nums[j]:
                nums[k] = left_nums[i]
                i+=1
                k+=1
            else:
                nums[k] = right_nums[j]
                j+=1
                k+=1
        
        while i< len(left_nums):
            nums[k] = left_nums[i]
            i+=1
            k+=1
        
        while j< len(right_nums):
            nums[k] = right_nums[j]
            j+=1
            k+=1
        return nums

        