# import math
# import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            heapq.heappush(min_heap, (math.sqrt(point[0]**2 + point[1]**2), point))
        return [heapq.heappop(min_heap)[1] for _ in range(k) ]