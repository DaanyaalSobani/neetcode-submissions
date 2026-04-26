class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            counter[n] = 1+ counter.get(n,0)
        
        heap = []
        for n in counter.keys():
            heapq.heappush(heap, (counter[n],n))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        