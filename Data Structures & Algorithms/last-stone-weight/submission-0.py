import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-x for x in stones]
        heapq.heapify(negative_stones)

        while len(negative_stones) > 1:
            stone_x = -heapq.heappop(negative_stones)
            stone_y = -heapq.heappop(negative_stones) if negative_stones else None
            if not stone_y:
                break
            if stone_x < stone_y:
                heapq.heappush(negative_stones, -(stone_y - stone_x))
            elif stone_x > stone_y:
                heapq.heappush(negative_stones, -(stone_x - stone_y))
        return -negative_stones[0] if negative_stones else 0