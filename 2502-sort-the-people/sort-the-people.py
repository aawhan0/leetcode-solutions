class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        for i in range(n-1):
            max_idx= i
            for j in range(i+1,n):
                if heights[j] > heights[max_idx]:
                    max_idx = j
            heights[i],heights[max_idx] = heights[max_idx],heights[i]
            # swapping the names as well, keeping the pairing intact
            names[i], names[max_idx] = names[max_idx], names[i]
        return names