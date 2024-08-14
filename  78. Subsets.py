class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = deque()
        q.append([])

        for el in nums:
            for i in range(len(q)):
                node = q.popleft()
                q.append(node+[el])
                q.append(node)
        return [q.popleft() for i in range(len(q))]
