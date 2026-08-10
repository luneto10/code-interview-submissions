class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = Counter(nums)
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res