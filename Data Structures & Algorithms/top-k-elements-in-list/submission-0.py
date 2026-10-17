class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
            numFreq[num] = 1 if num not in numFreq else numFreq[num] + 1
        keyVal = sorted(list(numFreq.items()), key=lambda x:x[1])
        ret = []
        for i in range(len(keyVal) - 1, len(keyVal) - k - 1, -1):
            ret.append(keyVal[i][0])
        return ret
