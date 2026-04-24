class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n in counter:
                counter[n]+=1
            else:
                counter[n]=1
        inverse_counter = defaultdict(list)
        keys = []
        for key in counter:
            inverse_counter[counter[key]].append(key)
            keys.append(counter[key])
        keys.sort()
        keys.reverse()
        result = []
        print(counter)
        i = 0
        while i < k:
           result.append(inverse_counter[keys[i]])
           i = i + len(inverse_counter[keys[i]])
        print(result)
        print(inverse_counter)
        actual_result = []
        for r in result:
            for i in range(len(r)):
                actual_result.append(r[i])
        return actual_result


        