class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        q = deque()
        q.append([])
        nums.sort()
        for i in range(len(nums)):
            lenth = len(q)
            for j in range(lenth):
                node = q.popleft()
                q.append(node + [nums[i]])
                
                if nums[i] not in node: 
                    q.append(node)
        return [q.popleft() for i in range(len(q))]
