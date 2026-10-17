class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        for char in t:
            if char not in freq:
                return False
            freq[char] -= 1
            if freq[char] == 0:
                freq.pop(char, None)
        return not freq