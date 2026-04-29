class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #O(n)
        res = [0] * len(nums)
        prod,zero_count = 1,0
        for num in nums:
            if num == 0:
                zero_count+=1
            else:
                prod *= num
        if zero_count>1:
            return res
        
        
        for i,n in enumerate(nums):
            if zero_count == 1:
                if n==0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // n
        return res


        