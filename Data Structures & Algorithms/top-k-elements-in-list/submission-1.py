class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = {}
        for num in nums:
            numFreq[num] = 1 if num not in numFreq else numFreq[num] + 1
        buckets = [[] for _ in range(len(nums))]
        for num, freq in numFreq.items():
            buckets[freq - 1].append(num)
        topK = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                topK.append(num)
                k -= 1
                if k == 0:
                    return topK
        return topK

