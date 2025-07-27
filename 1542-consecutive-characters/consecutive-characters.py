class Solution:
    def maxPower(self, s: str) -> int:
        max_power = 1
        current_power = 1

        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                current_power += 1
            else:
                max_power = max(current_power, max_power)
                current_power = 1
        return max(max_power, current_power)