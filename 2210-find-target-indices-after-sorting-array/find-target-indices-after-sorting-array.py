class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            minm = i
            for j in range(i,n):
                if nums[minm] > nums[j]:
                    minm = j
            nums[i], nums[minm] = nums[minm], nums[i]
        result = []
        for i in range(n):
            if nums[i] == target:
                result.append(i)
        return result 
