class Solution:
    def clear_alphabet(self,array):
        for i in range(len(array)):
            array[i]=0
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alphabet = [0,] * 26
        words = defaultdict(list)
        for word in strs:
            self.clear_alphabet(alphabet)
            for c in word:
                alphabet[ord(c) - ord('a')]+=1
            words[tuple(alphabet)].append(word)
        return [group for group in words.values()]


        