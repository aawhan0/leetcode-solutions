class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        majority_count = len(nums) // 2
        for i in nums:
            hashmap[i] = hashmap.get(i, 0) + 1
            if hashmap[i] > majority_count:
                return i