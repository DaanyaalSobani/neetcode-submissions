class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        result = []
        group_number=0
        for word in strs:
            counter = [0] * 26
            for c in word:
                counter[ord(c)-ord('a')] +=1
            t_counter = tuple(counter)
            if t_counter in d:
                result[d[t_counter]].append(word)
            else:
                d[tuple(counter)] = group_number
                result.append([word])
                group_number+=1
        return result