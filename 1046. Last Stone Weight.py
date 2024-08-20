class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * el for el in stones]
        heapq.heapify(stones)
        while len(stones) > 1: 
            fst, snd = heapq.heappop(stones), heapq.heappop(stones)
            if snd - fst > 0:
                heapq.heappush(stones, fst - snd)
        if stones:
            return - stones[0]
        return 0
