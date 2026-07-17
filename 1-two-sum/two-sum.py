class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        
        # this was brute force approach


        n = len(nums)
        hashmap = {}
        for i in range(n):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i