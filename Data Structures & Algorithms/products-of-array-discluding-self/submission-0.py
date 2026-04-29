class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       # O(n^2) solution
        p = 1
        result = []
        for i in range(len(nums)):
            p = 1
            for j,num in enumerate(nums):
                if i==j:
                    continue
                p *= num
            result.append(p)
        return result
        