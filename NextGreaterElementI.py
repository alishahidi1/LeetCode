class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = [nums2[-1]]
        dct_ans = {nums2[-1]:-1}
        n = len(nums2)

        for i in range (-2,-n-1,-1):
            if nums2[i] < stack[-1]:
                dct_ans[nums2[i]] = stack[-1]
                stack.append(nums2[i])
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack:
                    dct_ans[nums2[i]] = stack[-1]
                else:
                    dct_ans[nums2[i]] = -1
                stack.append(nums2[i])
        
        res =[]
        for num in nums1:
            res.append(dct_ans[num])
        return res
