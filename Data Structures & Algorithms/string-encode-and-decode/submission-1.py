class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedWord = []
        for word in strs:
            encodedStr = f"{len(word)}# {word}"
            encodedWord.append(encodedStr)
        return "".join(encodedWord)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = j = 0
        while j < len(s):
            if s[j] == "#":
                prefixLength = int(s[i:j])
                i = j + 2
                j = i + prefixLength
                decoded.append(s[i:j])
                i = j
            else:
                j += 1
        return decoded
