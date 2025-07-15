class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False

        for char in word:
            if not char.isalnum():  # Not a letter or digit
                return False
            if char.isalpha():
                if char.lower() in "aeiou":
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
