class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(n^2) solution:
        length = len(numbers)

        for i,n in enumerate(numbers):
            for j in range(i,length):
                if (n + numbers[j]) == target:
                    return [i+1,j+1]