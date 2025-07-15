class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        if n == 0:
            return 0

        total_possibilities = 1  # For the case where no key was pressed too long

        # We need to find segments of repeated characters
        # And for each segment of length L > 1, it contributes L-1 possibilities
        # for the case where exactly one key was pressed too long.

        i = 0
        while i < n:
            j = i
            # Find the end of the current block of identical characters
            while j < n and word[j] == word[i]:
                j += 1

            # Length of the current block
            block_length = j - i

            # If the block has more than one character, it means it could have
            # been formed by an accidental long press, and the number of ways
            # to reduce it is (block_length - 1).
            if block_length > 1:
                total_possibilities += (block_length - 1)

            # Move to the next block
            i = j

        return total_possibilities