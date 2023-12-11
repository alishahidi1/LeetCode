class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct = {0:1}
        res = 0
        s = 0
        
        for i in range(len(nums)):
            s += nums[i]
            if s - k in dct.keys():
                res += dct[s-k]
            if s in dct.keys():
                dct[s] += 1
            else:
                dct[s] = 1
        return res
