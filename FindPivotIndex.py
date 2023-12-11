class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        s = sum(nums)

        pref = 0
        post = s - nums[0]

        for i in range(n):
            if i == 0:
                pass
            else:
                pref = pref + nums [i-1]
                post = post - nums[i]
            if pref == post:
                return i
        return -1


