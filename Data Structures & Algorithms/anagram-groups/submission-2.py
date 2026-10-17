class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramsGrouped = {}
        for s in strs:
            sortWord = "".join(sorted(s))
            if sortWord in anagramsGrouped:
                anagramsGrouped[sortWord].append(s)
            else:
                anagramsGrouped[sortWord] = [s]
        ret = []
        for sortWord in anagramsGrouped.keys():
            ret.append(anagramsGrouped[sortWord])
        return ret