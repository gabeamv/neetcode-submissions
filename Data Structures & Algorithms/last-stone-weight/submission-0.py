import heapq
import math
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            diff = abs(x - y)
            if diff != 0:
                heapq.heappush_max(stones, diff)
        return 0 if not stones else stones[0]


        