class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter = defaultdict(list)
        
        for word in strs:
            counting_array = [0]*26
            for c in word:
                counting_array[ord(c)-ord('a')]+=1
            counter[tuple(counting_array)].append(word)
        return [v for k,v in counter.items()]