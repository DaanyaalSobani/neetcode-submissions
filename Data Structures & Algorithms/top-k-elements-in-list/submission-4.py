class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0)+1
        
        bucket = [[] for x in range(len(nums)+1)]
        
        for i,v in counter.items():
            bucket[v].append(i)

        result = []
        for l in reversed(bucket):
            for number in l:
                result.append(number)
                if len(result)==k:
                    return result
        
        