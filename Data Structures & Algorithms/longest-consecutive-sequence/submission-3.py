class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) in [0,1]:
            return len(nums)
        numbers_set = set(nums)
        sequence_starters=[]
        for n in nums:
            if n-1 not in numbers_set:
                sequence_starters.append(n)
        current_sequence = 1
        max_sequence = 1
        print(sequence_starters)
        for n in sequence_starters:
            k = n+1
            current_sequence=1
            while k in numbers_set:
                k+=1
                current_sequence+=1
            if current_sequence>max_sequence:
                max_sequence = current_sequence
        return max_sequence
        