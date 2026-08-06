from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key, v in counter.items():
            heap.append((-v, key))
        heapq.heapify(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res