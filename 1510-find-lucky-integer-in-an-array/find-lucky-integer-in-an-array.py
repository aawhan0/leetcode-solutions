class Solution:
	def findLucky(self, arr: List[int]) -> int:
		counts = {}
		for num in arr:
			counts[num] = counts.get(num, 0) +1
		max_lucky_num = -1
		
		for num,freq in counts.items():
			if num==freq:
				if num> max_lucky_num:
					max_lucky_num = num

		return max_lucky_num