class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pref = [0]*n
        post = [0]*n

        pref[0] = nums[0]
        post[-1] = nums[-1]

        for i in range(1,n):
            pref[i] = pref[i-1]*nums[i]
            j = -i-1
            post[j] = post[j+1]*nums[j]
        
        # for i in range(-2,-n-1,-1):
        #     post[i] = post[i+1]*nums[i]

        result = [0]*n
        result[0] = post[1]
        result[-1] = pref[-2]
        
        for i in range(1,n-1):
            result[i] = pref[i-1]*post[i+1]
        
        return result
            

          
